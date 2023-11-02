extends Node3D
class_name Game

@export var player: Player
@export var ui: UI

@onready var terrain: GridMap = $/root/Game/TestingLevel/Terrain

@onready var space := get_world_3d()
@onready var camera := get_viewport().get_camera_3d()
@onready var meshLibrary := terrain.mesh_library

var terrainLastHighlighted: Dictionary = {
	"position" = Vector3i.ZERO,
	"blockId" = -1,
	"orientation" = 0.0
	}
	
var terrainBlockLastHighlightedId: int
var grassBlockId: int
var highlightGrassBlockId: int

var mouseMovementDebugTimer: float = 0

# Called when the node enters the scene tree for the first time.
func _ready():
	grassBlockId = meshLibrary.find_item_by_name("Block")
	highlightGrassBlockId = meshLibrary.find_item_by_name("BlockSnow")
	
	# HOW TO CONNECT SIGNALS EXAMPLE
	# player.healthUpdate.connect(ui.updateHealth)

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	updateTimers(delta)
	handleMouseMovement()

func updateTimers(delta):
	mouseMovementDebugTimer += delta


func handleMouseMovement():
	var mouse_pos = get_viewport().get_mouse_position()
	var space = get_world_3d().direct_space_state
	
	var ray_length = 100
	
	var ray_query = PhysicsRayQueryParameters3D.new()
	ray_query.collision_mask = 2
	ray_query.from = camera.project_ray_origin(mouse_pos)
	ray_query.to = ray_query.from + camera.project_ray_normal(mouse_pos) * ray_length
	
	var raycast_result = space.intersect_ray(ray_query)
	
	if !('position' in raycast_result):
		return
	var position = raycast_result.position
	var oneYAboveTerrainPosition := terrain.local_to_map(position)
	var terrainPosition := Vector3i(oneYAboveTerrainPosition.x, oneYAboveTerrainPosition.y -1, oneYAboveTerrainPosition.z)
	
	var doesCellContainItem: bool = (terrain.get_cell_item(terrainPosition) != -1)
	if doesCellContainItem && terrainLastHighlighted["position"] != terrainPosition:
		print(terrainPosition)
		# revert previous cell item (un-highlight)
		terrain.set_cell_item(terrainLastHighlighted["position"], terrainLastHighlighted["blockId"], terrainLastHighlighted["orientation"])
		# record new cell item before highlighting it
		terrainLastHighlighted["position"] = terrainPosition
		terrainLastHighlighted["blockId"] = terrain.get_cell_item(terrainPosition)
		terrainLastHighlighted["orientation"] = terrain.get_cell_item_orientation(terrainPosition)
		# set new cell item (highlight)
		terrain.set_cell_item(terrainPosition, highlightGrassBlockId, terrain.get_cell_item_orientation(terrainPosition))

		

#		print(terrainLastHighlighted)
	
#	if terrainLastHighlighted["position"] != terrainPosition:
#		terrain.set_cell_item(terrainLastHighlighted["position"], terrainLastHighlighted["blockId"], terrainLastHighlighted["orientation"])
#	print(terrainPosition)
#	terrain.set_cell_item(terrainPosition, highlightBlockId, terrain.get_cell_item_orientation(terrainPosition))
