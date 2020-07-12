# File: model/__init__.py
# Description: the file constructs the model package for import

# Defines which backend is used
backend = "sqlite"

if backend == "sqlite":
	from .model_sqlite import model
elif backend == "dynamodb":
	from .model_dynamodb import model
else:
	raise ValueError("No appropriate database configured")

appmodel = model()

# Returns the model used in the app
def get_model():
	"""
	Gets the model used in the app
	:return: the model object
	"""
	return appmodel