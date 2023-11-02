extends RigidBody3D
class_name Player

signal healthUpdate(healthModifier)

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	var input := Vector3.ZERO
	input.x = Input.get_axis("ui_left", "ui_right")
	input.z = Input.get_axis("ui_up", "ui_down")
	
	apply_central_force(input * 1200.0 * delta)
	Transform3D()
	
	#var posdsdsition = get_global_mouse_position().snapped(Vector3(1,1,1))

func updateHealth(healthModifier):
	healthUpdate.emit(healthModifier)
