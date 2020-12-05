import bpy

# Name objects
ground = bpy.data.objects['Ground']
faller = bpy.data.objects['Obj']

def physics():
    # Deselect all
    bpy.ops.object.select_all(action='DESELECT')

    # Set up ground physics
    bpy.context.scene.objects.active = ground
    bpy.ops.rigidbody.object_add()
    ground.rigid_body.collision_shape = 'MESH'
    ground.rigid_body.type = 'ACTIVE'
    ground.rigid_body.enabled = False

    # Set up faller physics
    bpy.context.scene.objects.active = faller
    bpy.ops.rigidbody.object_add()
    faller.rigid_body.collision_shape = 'MESH'
    faller.rigid_body.type = 'ACTIVE'

    # Set scene length
    bpy.data.scenes['Scene'].frame_start = 1
    bpy.data.scenes['Scene'].frame_end = 250 # 5 seconds
    bpy.context.scene.rigidbody_world.point_cache.frame_start \
        = bpy.data.scenes['Scene'].frame_start
    bpy.context.scene.rigidbody_world.point_cache.frame_end \
        = bpy.data.scenes['Scene'].frame_end

    # Jump to start
    # bpy.ops.screen.frame_jump(end=False)

def sim():
    # Run sim/build cache
    bpy.ops.ptcache.bake_all(bake=True)
    # faller.select = True;
    # bpy.context.scene.objects.active = faller
    # bpy.ops.rigidbody.bake_to_keyframes()
    
    # Jump to end
    bpy.ops.screen.frame_jump(end=True)

def render(name="render", end=False, samples=None, animation=False):
    if end:
        # Jump to end
        bpy.ops.screen.frame_jump(end=True)

    if samples != None:
        bpy.context.scene.cycles.samples = samples

    # Render and save
    bpy.context.scene.render.filepath \
       = "/home/matt/clab/firstsim/render/{}.png".format(name)
        # = "/home/matt/clab/firstsim/render/blah.png"
    bpy.ops.render.render(write_still=True, use_viewport=True, animation=animation)

# Set up ground physics
# ground.game.physics_type = 'STATIC'
# ground.game.use_collision_bounds = True
# ground.game.collision_bounds_type = 'TRIANGLE_MESH'

# Set up faller physics
# faller.game.physics_type = 'RIGID_BODY'
# faller.game.use_collision_bounds = True
# faller.game.collision_bounds_type = 'TRIANGLE_MESH'



# Select ground

# ground.select = True

# Set up faller
# bpy.context.scene.objects.active = ground
# bpy.ops.rigidbody.object_add()
# faller.rigid_body.collision_shape = 'MESH'

# Set up ground


# bpy.ops.surface.primitive_nurbs_surface_sphere_add()
