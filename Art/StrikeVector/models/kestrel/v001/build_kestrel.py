"""Reference-led Kestrel art prototype. Blender 4.5. No engine/gameplay edits.
Run: Blender -b --factory-startup --python /absolute/path/build_kestrel.py
The inferred underside and exact dimensions are proposals, not a reconstruction claim.
"""
import bpy, math, random, json
from pathlib import Path
from mathutils import Vector

OUT=Path(__file__).resolve().parent
R=OUT/'renders';R.mkdir(exist_ok=True)
random.seed(21)
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
asset=bpy.data.collections.new('SV_Kestrel_ArtPrototype');bpy.context.scene.collection.children.link(asset)
studio=bpy.data.collections.new('STUDIO_not_exported');bpy.context.scene.collection.children.link(studio)
def move(o,col=asset):
 for c in list(o.users_collection):c.objects.unlink(o)
 col.objects.link(o);return o
def rgb(h):
 vals=[int(h[i:i+2],16)/255 for i in (1,3,5)]
 return tuple(v/12.92 if v<.04045 else ((v+.055)/1.055)**2.4 for v in vals)
def mat(name,h,metal=0,rough=.75,emit=0,wear=False):
 m=bpy.data.materials.new(name);m.diffuse_color=(*rgb(h),1);m.use_nodes=True
 n=m.node_tree.nodes;l=m.node_tree.links;p=n.get('Principled BSDF')
 p.inputs['Base Color'].default_value=m.diffuse_color;p.inputs['Metallic'].default_value=metal;p.inputs['Roughness'].default_value=rough
 if emit:p.inputs['Emission Color'].default_value=m.diffuse_color;p.inputs['Emission Strength'].default_value=emit
 if wear:
  tex=n.new('ShaderNodeTexNoise');tex.inputs['Scale'].default_value=32;tex.inputs['Detail'].default_value=1.5;tex.inputs['Roughness'].default_value=.7
  coord=n.new('ShaderNodeTexCoord');l.new(coord.outputs['Generated'],tex.inputs['Vector'])
  ramp=n.new('ShaderNodeValToRGB');ramp.color_ramp.elements[0].position=.64;ramp.color_ramp.elements[0].color=m.diffuse_color
  ramp.color_ramp.elements[1].position=.76;ramp.color_ramp.elements[1].color=(*rgb('#625849'),1)
  l.new(tex.outputs['Fac'],ramp.inputs[0]);l.new(ramp.outputs[0],p.inputs['Base Color'])
 return m
BONE=mat('SV_Paint_DirtyBone','#C4BAA2',wear=True)
GOLD=mat('SV_Paint_Mustard','#C18A32',wear=True)
OXIDE=mat('SV_Paint_OxideRepair','#9F4938',wear=True)
FRAME=mat('SV_Frame_Graphite','#30383B',.7,.57)
DARK=mat('SV_Recess_Black','#111B1E',.1,.82)
RUBBER=mat('SV_Service_Rubber','#202527',0,.88)
GLASS=mat('SV_Canopy_Smoked','#26353E',.3,.3)
METAL=mat('SV_Fastener_Steel','#7B817D',.8,.5)
LIGHT=mat('SV_Energy_Mint','#79DDD0',.1,.35,6)
CORE=mat('SV_Energy_Core','#C3FFF1',0,.3,10)
INK=mat('SV_Ink_Mustard','#BB8735',0,.9)
LIME=mat('SV_Ink_CrewAccent','#C9D657',0,.9)
def mesh(name,verts,faces,material,bevel=0):
 me=bpy.data.meshes.new(name);me.from_pydata(verts,[],faces);me.update()
 o=bpy.data.objects.new(name,me);asset.objects.link(o);o.data.materials.append(material)
 if bevel:
  b=o.modifiers.new('Small physical edge bevel','BEVEL');b.width=bevel;b.segments=2
  b.affect='EDGES'
  n=o.modifiers.new('Weighted planar normals','WEIGHTED_NORMAL');n.keep_sharp=True;n.weight=40
 return o
def box(name,loc,dim,m,bevel=.025):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=move(bpy.context.object);o.name=name;o.dimensions=dim
 bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.append(m)
 if bevel:
  b=o.modifiers.new('Beveled edges','BEVEL');b.width=bevel;b.segments=2
  o.modifiers.new('Weighted normals','WEIGHTED_NORMAL')
 return o
def section(cx,y,w,z0,z1,ch):
 return [(cx-w/2+ch,y,z0),(cx+w/2-ch,y,z0),(cx+w/2,y,z0+ch),(cx+w/2,y,z1-ch),(cx+w/2-ch,y,z1),(cx-w/2+ch,y,z1),(cx-w/2,y,z1-ch),(cx-w/2,y,z0+ch)]
def loft(name,sections,m,cap_start=True,cap_end=True,bevel=.008):
 vs=[p for s in sections for p in s];fs=[]
 for j in range(len(sections)-1):
  for i in range(8):fs.append((j*8+i,j*8+(i+1)%8,(j+1)*8+(i+1)%8,(j+1)*8+i))
 if cap_start:fs.append(tuple(range(7,-1,-1)))
 if cap_end:fs.append(tuple((len(sections)-1)*8+i for i in range(8)))
 return mesh(name,vs,fs,m,bevel)
def ring(name,cx,y,ow,oz0,oz1,iw,iz0,iz1,depth,m):
 outer=section(cx,y,ow,oz0,oz1,.1);inner=section(cx,y,iw,iz0,iz1,.055)
 far=section(cx,y+depth,iw,iz0,iz1,.055);vs=outer+inner+far;fs=[]
 for i in range(8):
  j=(i+1)%8;fs += [(i,j,8+j,8+i),(8+i,8+j,16+j,16+i)]
 return mesh(name,vs,fs,m,.008)
def tube(name,pts,r,m,res=2):
 cu=bpy.data.curves.new(name,'CURVE');cu.dimensions='3D';cu.resolution_u=12;cu.bevel_depth=r;cu.bevel_resolution=res
 sp=cu.splines.new('BEZIER');sp.bezier_points.add(len(pts)-1)
 for b,p in zip(sp.bezier_points,pts):b.co=p;b.handle_left_type='AUTO';b.handle_right_type='AUTO'
 o=bpy.data.objects.new(name,cu);asset.objects.link(o);o.data.materials.append(m);return o
def cylinder(name,loc,r,depth,m,direction=(0,0,1),vertices=10):
 bpy.ops.mesh.primitive_cylinder_add(vertices=vertices,radius=r,depth=depth,location=loc);o=move(bpy.context.object);o.name=name
 o.rotation_euler=Vector(direction).to_track_quat('Z','Y').to_euler();o.data.materials.append(m);return o

# Underbody: intentionally simple inferred assembly, largely hidden in hero view.
loft('Central_structural_keel',[section(0,-2.45,2.5,.18,.72,.17),section(0,-.8,2.3,.13,.78,.17),section(0,.32,.8,.2,.65,.12)],FRAME,bevel=.02)
box('Rear_transverse_bridge',(0,-2.12,.82),(2.6,.62,.4),FRAME,.065)
for x in [-.45,0,.45]:box('Bridge_service_panel',(x,-2.12,1.027),(.4,.49,.025),FRAME,.015)

# Primary rails: chamfered variable cross-sections with an actual open front throat.
railprofiles=[(-1.25,1.08,.2,.95),(-.45,1.14,.15,1.09),(.75,1.08,.12,1.02),(1.8,1.04,.14,.9),(2.8,.96,.19,.68)]
for s in [-1,1]:
 cx=s*1.04;side='L' if s<0 else 'R'
 loft(f'{side}_dark_inner_chassis',[section(cx,y,w*.95,z0-.04,z1-.09,.12) for y,w,z0,z1 in railprofiles],FRAME,bevel=.025)
 # Main paint volumes stop at front aperture rather than covering it.
 loft(f'{side}_primary_armor',[section(cx,y,w,z0,z1,.14) for y,w,z0,z1 in railprofiles],BONE,cap_end=False,bevel=.015)
 ring(f'{side}_nose_armor_rim',cx,2.803,.96,.19,.68,.75,.265,.525,-.14,BONE)
 ring(f'{side}_nose_dark_throat',cx,2.815,.78,.245,.55,.66,.30,.47,-.22,FRAME)
 box(f'{side}_nose_cavity_back',(cx,2.57,.385),(.66,.025,.22),DARK,.008)
 box(f'{side}_front_running_light',(cx,2.745,.423),(.60,.025,.043),LIGHT,.009)
 box(f'{side}_front_light_core',(cx,2.762,.431),(.54,.008,.014),CORE,.004)
 # Raised shoulder covers: nonparallel step around cockpit and rear connection.
 loft(f'{side}_raised_shoulder',[section(s*.91,-1.42,1.05,.72,1.08,.12),section(s*.86,-.8,.99,.76,1.22,.15),section(s*.97,-.16,.77,.78,1.10,.12)],BONE,bevel=.018)
 # Sloping mustard band follows rail top and shoulder chamfer.
 for y0,y1 in [(1.16,1.45),(1.48,1.53)]:
  def top(y):return 1.02+(y-.75)*(.9-1.02)/(1.8-.75)
  w=1.06
  mesh(f'{side}_mustard_band',[(cx-w/2+.14,y0,top(y0)+.012),(cx+w/2-.14,y0,top(y0)+.012),(cx+w/2-.14,y1,top(y1)+.012),(cx-w/2+.14,y1,top(y1)+.012)],[(0,1,2,3)],GOLD)
  # Outboard vertical continuation of the band.
  x=cx+s*.53
  mesh(f'{side}_band_side',[(x,y0,.30),(x,y1,.30),(x,y1,top(y1)-.14),(x,y0,top(y0)-.14)],[(0,1,2,3)],GOLD)
 # Major panel seams: fine dark geometry in purposeful lengths.
 for y in [-.30,.55,1.80]:
  z=min(railprofiles,key=lambda p:abs(p[0]-y))[3]
  box(f'{side}_armor_seam',(cx,y,z+.003),(.77,.015,.008),FRAME,.001)
 # Inner ribbed service strip, low enough to maintain slot.
 for y in [.6,.92,1.24,1.56,1.88,2.2]:box(f'{side}_inner_rib',(cx-s*.49,y,.40),(.06,.09,.27),FRAME,.009)
 loft(f'{side}_under_hover_skid',[section(cx,-1.05,.65,.02,.19,.06),section(cx,2.35,.58,.05,.2,.06)],DARK,bevel=.016)
 # Large rear pod housing with an open throat at each end.
 ex=s*1.28
 loft(f'{side}_engine_shell',[section(ex,-2.8,.9,.26,1.25,.12),section(ex,-1.79,.9,.26,1.25,.12)],FRAME,cap_start=False,cap_end=False,bevel=.025)
 box(f'{side}_engine_top_armor',(ex,-2.28,1.264),(.68,.90,.035),BONE,.025)
 box(f'{side}_engine_top_band',(ex+.07,-2.28,1.287),(.19,.88,.008),GOLD,.008)
 for front,y,dep in [(True,-1.77,-.15),(False,-2.82,.15)]:
  desc='intake' if front else 'exhaust'
  ring(f'{side}_{desc}_rim',ex,y,.94,.23,1.28,.72,.37,1.13,dep,FRAME)
  ring(f'{side}_{desc}_inner_lip',ex,y+dep*.4,.74,.35,1.15,.62,.43,1.07,dep*.9,METAL)
  box(f'{side}_{desc}_dark_back',(ex,y+dep*1.8,.75),(.62,.03,.65),DARK,.01)
  for z in [.52,.69,.86]:box(f'{side}_{desc}_louver',(ex,y+dep*1.5,z),(.57,.04,.045),FRAME,.005)
  # Inset bracket strips, not entire illuminated engine face.
  side_x=ex+s*.29
  tube(f'{side}_{desc}_energy_bracket',[(side_x-s*.05,y+dep*.55,.46),(side_x,y+dep*.55,.51),(side_x,y+dep*.55,1.01),(side_x-s*.05,y+dep*.55,1.06)],.026,LIGHT,1)
  if not front:box(f'{side}_rear_energy_core',(ex,y+dep*.7,.73),(.38,.024,.07),CORE,.015)
 # Ribbed hose. Closely spaced collars along a deliberate arch.
 pts=[(s*.78,-.72,1.03),(s*.80,-1.06,1.28),(s*.91,-1.48,1.38),(s*1.0,-1.94,1.37)]
 tube(f'{side}_service_hose',pts,.105,RUBBER,2)
 for k in range(14):
  t=k/13;y=-.78-t*1.1;x=s*(.78+.20*t);z=1.08+.31*math.sin(t*math.pi/2)
  cylinder(f'{side}_hose_rib_{k}',(x,y,z),.12,.028,RUBBER,(s*.15,-1,.25*(1-t)),12)
 cylinder(f'{side}_oxide_coupler',(s*1.0,-1.98,1.37),.145,.24,OXIDE,(0,1,0),12)
 cylinder(f'{side}_coupler_band',(s*1.0,-1.85,1.37),.15,.055,METAL,(0,1,0),12)
 # Body outer side dark cut-in and small service ribs.
 for y in [-.9,-.65,-.4]:box(f'{side}_side_recess',(cx+s*.56,y,.48),(.018,.15,.26),FRAME,.005)

# Canopy: faceted sloped glass nestled between shoulders, not an upright box.
canopy=[(-.40,.65,.68),(.40,.65,.68),(.47,-.8,.85),(-.47,-.8,.85),(-.28,-.18,1.34),(.28,-.18,1.34),(.30,-1.12,1.30),(-.30,-1.12,1.30)]
mesh('Cockpit_black_surround',canopy,[(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7),(4,5,6,7),(0,3,2,1)],FRAME,.027)
glassfront=[(-.335,.56,.73),(.335,.56,.73),(.245,-.16,1.299),(-.245,-.16,1.299)]
mesh('Windshield',glassfront,[(0,1,2,3)],GLASS,.008)
for s in [-1,1]:mesh('Canopy_side_glass',[(s*.415,-.69,.90),(s*.36,.44,.78),(s*.285,-.22,1.29),(s*.29,-1.02,1.25)],[(0,1,2,3)],GLASS,.006)
mesh('Canopy_roof_glass',[(-.24,-.28,1.349),(.24,-.28,1.349),(.255,-1.01,1.315),(-.255,-1.01,1.315)],[(0,1,2,3)],GLASS)
box('Cockpit_brow', (0,.63,.69),(.86,.11,.13),FRAME,.04)

# Asymmetric repairs around the left nose and rear right shoulder.
plate=mesh('L_oxide_repair_plate',[(-1.48,1.70,.76),(-.78,1.70,.94),(-.78,2.20,.83),(-1.48,2.20,.66),(-1.49,1.70,.42),(-1.49,2.20,.39)],[(0,1,2,3),(0,3,5,4)],OXIDE,.012)
box('R_shoulder_oxide_patch',(1.18,-.99,1.105),(.40,.36,.05),OXIDE,.022)
for s in [-1,1]:
 for y,z in [(2.12,.84),(1.78,.91),(.55,1.06),(-.45,1.12)]:
  for off in [-.30,.30]:cylinder('Armor_fastener',(s*1.04+off,y,z),.018,.013,METAL,vertices=8)

# Broad designed paint loss on top plates: sparse edge chips, real flat patches in GLB too.
for s in [-1,1]:
 for k in range(30):
  y=random.uniform(.78,2.6);t=(y-.75)/2.05;z=1.02-.34*t
  # Stay on the flat top inside the large chamfer.
  x=s*1.04+random.choice([-1,1])*random.uniform(.29,.34);rr=random.uniform(.012,.035)
  pts=[(x-rr,y-rr,z+.015),(x+rr*.8,y-rr*.6,z+.015),(x+rr,y+rr*.5,z+.015),(x-rr*.4,y+rr,z+.015)]
  mesh('Paint_edge_chip',pts,[(0,1,2,3)],FRAME)

# Original number painted on the outboard right panel. Text converted for export.
bpy.ops.object.text_add(location=(1.60,1.03,.48));o=move(bpy.context.object);o.name='Race_number_01'
o.data.body='01';o.data.size=.29;o.data.extrude=0;o.data.align_x='CENTER'
# local text X runs toward nose (Y); local Y runs up (Z); normal points +X.
from mathutils import Matrix
o.rotation_euler=Matrix(((0,0,1),(1,0,0),(0,1,0))).to_euler();o.data.materials.append(INK)
# Small crew accent on the left sloping upper nose, proportions from emission concept.
tag=[(-1.35,1.95,.877),(-1.02,2.07,.858),(-1.10,1.98,.873),(-.86,1.90,.887),(-1.10,1.75,.912),(-1.03,1.85,.895)]
mesh('Crew_arrow_paint',tag,[(0,1,2,3,4,5)],LIME)

# Unambiguous socket empties for later engine effects; no static trail geometry.
for s in [-1,1]:
 o=bpy.data.objects.new('FX_Rear_L' if s<0 else 'FX_Rear_R',None);asset.objects.link(o);o.location=(s*1.28,-2.85,.74);o.empty_display_size=.12

# Studio render setup is isolated and excluded from export.
floor=box('Studio_floor',(0,0,-.22),(200,200,.15),mat('Studio_floor_mat','#969486'),.0);move(floor,studio)
world=bpy.data.worlds.new('Neutral studio');bpy.context.scene.world=world;world.use_nodes=True;world.node_tree.nodes['Background'].inputs[0].default_value=(.35,.39,.42,1);world.node_tree.nodes['Background'].inputs[1].default_value=.65
def area(name,loc,energy,size,color):
 d=bpy.data.lights.new(name,'AREA');o=bpy.data.objects.new(name,d);studio.objects.link(o);o.location=loc;o.rotation_euler=(Vector((0,0,.6))-o.location).to_track_quat('-Z','Y').to_euler();d.energy=energy;d.shape='DISK';d.size=size;d.color=color
area('Warm key',(2,5,8),1600,5,(1,.88,.72));area('Cool fill',(-5,1,4),1000,6,(.68,.82,1));area('Rear rim',(2,-5,5),1800,4,(1,.94,.81))
camdata=bpy.data.cameras.new('ArtCamera');cam=bpy.data.objects.new('ArtCamera',camdata);studio.objects.link(cam);bpy.context.scene.camera=cam
scene=bpy.context.scene;scene.render.engine='CYCLES';scene.cycles.samples=32;scene.cycles.use_denoising=True
scene.render.resolution_x=1500;scene.render.resolution_y=1150;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG';scene.view_settings.view_transform='AgX'
scene.render.film_transparent=False
def camera(loc,target=(0,0,.7),ortho=None):
 cam.location=loc;cam.rotation_euler=(Vector(target)-cam.location).to_track_quat('-Z','Y').to_euler();camdata.type='ORTHO' if ortho else 'PERSP';camdata.lens=55
 if ortho:camdata.ortho_scale=ortho
camera((8,10,7.0))
scene.use_nodes=True;nt=scene.node_tree;nt.nodes.clear();rl=nt.nodes.new('CompositorNodeRLayers');gl=nt.nodes.new('CompositorNodeGlare');gl.glare_type='FOG_GLOW';gl.quality='HIGH';gl.threshold=1.5;gl.size=7;gl.mix=-.92;co=nt.nodes.new('CompositorNodeComposite');nt.links.new(rl.outputs['Image'],gl.inputs['Image']);nt.links.new(gl.outputs['Image'],co.inputs['Image'])
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'SV_Kestrel_ArtPrototype_v001.blend'))
scene.render.filepath=str(R/'Kestrel_front_v001.png');bpy.ops.render.render(write_still=True)
camera((-7,-10,6));scene.render.filepath=str(R/'Kestrel_rear_v001.png');bpy.ops.render.render(write_still=True)
# Orthographic evidence comes from this actual model, not imagined multi-view concept art.
scene.render.resolution_x=1000;scene.render.resolution_y=1000;scene.cycles.samples=16
for name,loc,target in [('top',(0,0,10),(0,0,0)),('front',(0,10,.75),(0,0,.75)),('side',(10,0,.75),(0,0,.75)),('rear',(0,-10,.75),(0,0,.75))]:
 camera(loc,target,7);scene.render.filepath=str(R/f'Kestrel_ortho_{name}_v001.png');bpy.ops.render.render(write_still=True)

# Export evaluated geometry. Procedural wear is Blender preview only; convert materials to flat palette for GLB.
bpy.ops.object.select_all(action='DESELECT')
for o in list(asset.objects):
 if o.type in {'MESH','CURVE','FONT'}:
  o.select_set(True);bpy.context.view_layer.objects.active=o
  if o.type!='MESH':bpy.ops.object.convert(target='MESH')
  for mod in list(o.modifiers):
   try:bpy.ops.object.modifier_apply(modifier=mod.name)
   except RuntimeError:pass
  o.select_set(False)
for m in bpy.data.materials:
 if m.use_nodes:
  p=m.node_tree.nodes.get('Principled BSDF')
  if p:
   for link in list(p.inputs['Base Color'].links):m.node_tree.links.remove(link)
   p.inputs['Base Color'].default_value=m.diffuse_color
for o in asset.objects:o.select_set(True)
bpy.ops.export_scene.gltf(filepath=str(OUT/'SV_Kestrel_ArtPrototype_v001.glb'),export_format='GLB',use_selection=True,export_apply=True,export_yup=True)
meshes=[o for o in asset.objects if o.type=='MESH'];tri=0
for o in meshes:o.data.calc_loop_triangles();tri+=len(o.data.loop_triangles)
coords=[o.matrix_world@Vector(v) for o in meshes for v in o.bound_box]
mins=[min(v[i] for v in coords) for i in range(3)];maxs=[max(v[i] for v in coords) for i in range(3)]
(OUT/'BUILD_REPORT.json').write_text(json.dumps({'status':'first art model, unapproved','blender':bpy.app.version_string,'source_axes':'X right, Y front, Z up','bounds_min':mins,'bounds_max':maxs,'dimensions_m':[maxs[i]-mins[i] for i in range(3)],'mesh_objects':len(meshes),'triangles':tri,'materials':len(set(m.name for o in meshes for m in o.data.materials)),'procedural_wear':'Blender preview only; GLB exports flat material colors plus modeled paint chips','engine_import_tested':False},indent=2))
print('KESTREL_BUILD_COMPLETE',tri,'triangles')
