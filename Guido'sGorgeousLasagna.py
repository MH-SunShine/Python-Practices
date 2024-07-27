# Constants
EXPECTED_BAKE_TIME = 40  # Expected bake time in minutes


# Functions
def bake_time_remaining(time_in_oven):
    """
    Calculate the bake time remaining.

    Parameters:
    time_in_oven (int): Time the lasagna has been in the oven.

    Returns:
    int: Remaining bake time.
    """
    return EXPECTED_BAKE_TIME - time_in_oven


def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the preparation time in minutes.

    Parameters:
    number_of_layers (int): Number of layers in the lasagna.

    Returns:
    int: Preparation time in minutes.
    """
    return number_of_layers * 2  # Assuming each layer takes 2 minutes


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the total elapsed cooking time (prep + bake) in minutes.

    Parameters:
    number_of_layers (int): Number of layers in the lasagna.
    elapsed_bake_time (int): Time the lasagna has been baking.

    Returns:
    int: Total elapsed cooking time.
    """
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time


# Example Usage
remaining_time_to_bake = bake_time_remaining(30)
print(f"Remaining bake time = {remaining_time_to_bake} minutes")

prep_time_for_3_layers = preparation_time_in_minutes(3)
print(f"Preparation time needed for 3 layers = {prep_time_for_3_layers} minutes")

total_cooking_time = elapsed_time_in_minutes(3, 20)
print(f"Total cooking time for 3 lasagna layers and 20 minutes of baking = {total_cooking_time} minutes")
