# Genera los humanos del juego (GLB con esqueleto) con MakeHuman (MPFB2) en Blender.
# Uso: blender -b --python tools/humanos.py -- [id ...]   (sin id: todos)
# Requiere la extensión MPFB2 y los asset packs CC0 (system assets, shirts01, pants01) instalados.
# Todo lo que usa es CC0 (MakeHuman Community).
import bpy, sys, os, re

from bl_ext.user_default.mpfb.services.humanservice import HumanService
from bl_ext.user_default.mpfb.services.assetservice import AssetService
from bl_ext.user_default.mpfb.services.exportservice import ExportService
from bl_ext.user_default.mpfb.services.objectservice import ObjectService

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ROOT, 'humanos')
DATA = AssetService.get_available_data_roots()

HUMANOS = {
    # el Dr. Hale: americano, cuarenta y tantos, chaleco de lana gris y pantalón de paño
    'hale': dict(macro=dict(gender=1, age=.62, muscle=.5, weight=.55, height=.55, proportions=.6, race=dict(caucasian=1, asian=0, african=0)),
                 skin='skins/middleage_caucasian_male/middleage_caucasian_male.mhmat',
                 clothes=['clothes/toigo_fisherman_sweater/toigo_fisherman_sweater.mhclo', 'clothes/toigo_wool_pants/toigo_wool_pants.mhclo', 'clothes/shoes02/shoes02.mhclo'],
                 tint={'toigo_fisherman_sweater': (.42, .43, .42), 'toigo_wool_pants': (.32, .3, .27)},
                 hair='hair/short02/short02.mhclo', brows='eyebrows/eyebrow001/eyebrow001.mhclo'),
    # un marinero del 83: joven, flaco, la roba azul de a bordo
    'marinero': dict(macro=dict(gender=1, age=.45, muscle=.55, weight=.38, height=.5, proportions=.55, race=dict(caucasian=1, asian=0, african=0)),
                     skin='skins/young_caucasian_male/young_caucasian_male.mhmat',
                     clothes=['clothes/male_worksuit01/male_worksuit01.mhclo', 'clothes/shoes01/shoes01.mhclo'],
                     tint={'male_worksuit01': (.16, .22, .34), 'shoes01': (.25, .22, .2)},
                     hair='hair/short04/short04.mhclo', brows='eyebrows/eyebrow010/eyebrow010.mhclo'),
}


def find(frag):
    for r in DATA:
        p = os.path.join(r, frag)
        if os.path.exists(p): return p
    raise FileNotFoundError(frag)


def mhmat_textures(path):
    t = {}
    for line in open(path, encoding='utf-8', errors='ignore'):
        m = re.match(r'\s*(diffuseTexture|normalmapTexture|bumpTexture|transparencyMapTexture)\s+(\S+)', line)
        if m: t[m.group(1)] = os.path.normpath(os.path.join(os.path.dirname(path), m.group(2)))
    return t


def principled(name, tex, alpha=False, rough=.8):
    # material simple (Principled + texturas) para que el exportador glTF lo entienda
    m = bpy.data.materials.new(name); m.use_nodes = True
    nt = m.node_tree; bs = nt.nodes['Principled BSDF']; bs.inputs['Roughness'].default_value = rough
    if 'diffuseTexture' in tex and os.path.exists(tex['diffuseTexture']):
        im = nt.nodes.new('ShaderNodeTexImage'); im.image = bpy.data.images.load(tex['diffuseTexture'], check_existing=True)
        nt.links.new(im.outputs['Color'], bs.inputs['Base Color'])
        if alpha:
            nt.links.new(im.outputs['Alpha'], bs.inputs['Alpha']); m.blend_method = 'HASHED' if hasattr(m, 'blend_method') else None
    if 'bumpTexture' in tex and 'normalmapTexture' not in tex and tex['bumpTexture'].upper().endswith('NORM.PNG'): tex['normalmapTexture'] = tex['bumpTexture']
    if 'normalmapTexture' in tex and os.path.exists(tex['normalmapTexture']):
        im = nt.nodes.new('ShaderNodeTexImage'); im.image = bpy.data.images.load(tex['normalmapTexture'], check_existing=True); im.image.colorspace_settings.name = 'Non-Color'
        nm = nt.nodes.new('ShaderNodeNormalMap'); nt.links.new(im.outputs['Color'], nm.inputs['Color']); nt.links.new(nm.outputs['Normal'], bs.inputs['Normal'])
    return m


def tint(mat, rgb):
    # tiñe la textura difusa: conserva el tejido (luminancia) y cambia el color
    import numpy as np
    for n in mat.node_tree.nodes:
        if n.type == 'TEX_IMAGE' and n.image and n.image.colorspace_settings.name != 'Non-Color':
            im = n.image.copy(); im.name = mat.name + '_tinte'
            px = np.empty(len(im.pixels), dtype=np.float32); im.pixels.foreach_get(px); px = px.reshape(-1, 4)
            l = (px[:, 0] * .3 + px[:, 1] * .59 + px[:, 2] * .11)
            l = l / max(float(np.percentile(l, 90)), 1e-3)
            for k in range(3): px[:, k] = np.clip(l * rgb[k] * 1.6, 0, 1)
            im.pixels.foreach_set(px.ravel()); im.update(); n.image = im
            return


def set_mat(obj, mat):
    obj.data.materials.clear(); obj.data.materials.append(mat)


def build(hid, spec):
    # escena vacía (sin read_factory_settings: descargaría la extensión)
    for o in list(bpy.data.objects): bpy.data.objects.remove(o, do_unlink=True)
    for coll in (bpy.data.meshes, bpy.data.armatures, bpy.data.materials, bpy.data.images):
        for d in list(coll): coll.remove(d)
    macro = spec['macro']
    bm = HumanService.create_human(macro_detail_dict=dict(cupsize=.5, firmness=.5, **macro))
    rig = HumanService.add_builtin_rig(bm, 'game_engine')
    skin = find(spec['skin'])
    HumanService.set_character_skin(skin, bm, skin_type='MAKESKIN')
    set_mat(bm, principled(hid + '_piel', mhmat_textures(skin), rough=.6))
    parts = [(c, 'Clothes', False) for c in spec['clothes']]
    parts += [(spec['hair'], 'Hair', True), (spec['brows'], 'Eyebrows', True),
              ('eyes/low-poly/low-poly.mhclo', 'Eyes', False), ('eyelashes/eyelashes02/eyelashes02.mhclo', 'Eyelashes', True)]
    for frag, kind, alpha in parts:
        p = find(frag)
        o = HumanService.add_mhclo_asset(p, bm, asset_type=kind, subdiv_levels=0, material_type='MAKESKIN')
        mh = os.path.splitext(p)[0] + '.mhmat'
        cand = [mh] + [os.path.join(os.path.dirname(p), f) for f in os.listdir(os.path.dirname(p)) if f.endswith('.mhmat')]
        if kind == 'Eyes': cand = [find('eyes/materials/brown.mhmat')]
        tex = mhmat_textures(next(c for c in cand if os.path.exists(c)))
        name = os.path.basename(os.path.dirname(p))
        mat = principled(hid + '_' + kind.lower() + '_' + name, tex, alpha=alpha, rough=.35 if kind == 'Eyes' else .85)
        if name in spec.get('tint', {}): tint(mat, spec['tint'][name])
        set_mat(o, mat)
    # aplica máscaras de ropa y quita los helpers: queda solo lo visible
    ExportService.bake_modifiers_remove_helpers(bm, bake_masks=True, bake_subdiv=False, remove_helpers=True)
    for o in bpy.data.objects:
        if o.type == 'MESH':
            for mod in [m for m in o.modifiers if m.type != 'ARMATURE']:
                bpy.context.view_layer.objects.active = o
                try: bpy.ops.object.modifier_apply(modifier=mod.name)
                except Exception as e: print('mod', o.name, mod.name, e)
            if o.data.shape_keys:
                # hornea la forma (sexo, edad, peso…) en la malla; borrar las shape keys la devolvería al cuerpo neutro
                bpy.context.view_layer.objects.active = o
                bpy.ops.object.shape_key_remove(all=True, apply_mix=True)
    for img in bpy.data.images:
        if img.size[0] > 1024: img.scale(1024, int(1024 * img.size[1] / img.size[0]))
    os.makedirs(OUT, exist_ok=True)
    out = os.path.join(OUT, hid + '.glb')
    bpy.ops.export_scene.gltf(filepath=out, export_format='GLB', export_skins=True, export_animations=False, export_morph=False,
                              export_image_format='WEBP', export_image_quality=80, export_apply=False, export_yup=True)
    nv = sum(len(o.data.vertices) for o in bpy.data.objects if o.type == 'MESH')
    print('OK', hid, out, os.path.getsize(out) // 1024, 'KB', nv, 'verts', [b.name for b in rig.data.bones][:60])


ids = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
for k, v in HUMANOS.items():
    if not ids or k in ids: build(k, v)
