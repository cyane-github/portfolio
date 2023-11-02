extends CanvasLayer
class_name UI

@onready var health_label = $Control/MarginContainer/VBoxContainer/HBoxContainer/Health

var health = 0:
	set(new_health):
		health = new_health
		updateHealthLabel()

# Called when the node enters the scene tree for the first time.
func _ready():
	updateHealthLabel()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func updateHealthLabel():
	health_label.text = "HP: " + str(health)

func onHealthUpdate(healthModifier) -> void:
	health += healthModifier
