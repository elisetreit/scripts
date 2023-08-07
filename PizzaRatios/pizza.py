import argparse
def pizzaRecipe(hydration = 0.66, salt = 0.02, dough_balls = 8, dough_ball_weight = 6, unit = "oz"):
    """
    Prints a pizza recipe based on parameters such as hydration and number of dough balls
    ----------
    Parameters
    ----------
    hydration : float (default 0.66)
        The hydration of the dough, or the ratio of water to flour, expressed as a decimal
    salt : float (default 0.02)
        The salt percentage of the dough, or the ratio of salt to flour, expressed as a decimal
    dough_balls : int (default 8)
        The number of dough balls to make
    dough_ball_weight : int (default 6)
        The weight of each dough ball in specified units
    unit : str (default "oz")
        The unit of measure for the dough ball weight - either "oz" or "g"
    """

    # 1. Calculate total dough weight
    if unit == "oz":
        total_weight = dough_balls * dough_ball_weight * 28.3495
    elif unit == "g":
        total_weight = dough_balls * dough_ball_weight
    else:
        print("Invalid unit")
    # preferment ratio
    r = 560/1360
    preferment_weight = total_weight * r
    print(f"making {round(preferment_weight)} grams preferment")
    preferment_flour = preferment_weight / (1+hydration)
    preferment_water = preferment_flour * hydration
    print(f"Mix {round(preferment_flour)} grams flour and {round(preferment_water)} grams water with 1/8 tsp yeast")
    print(f"Let sit at room temperature overnight - this is your preferment")
    # final dough
    total_flour = total_weight / (1 + hydration + salt)
    final_flour = total_flour - preferment_flour
    final_water = final_flour * hydration
    final_salt = final_flour * salt
    print(f"Mix {round(final_flour)} grams flour, {round(final_water)} grams water, {round(final_salt)} grams salt, and a little oil if you are using bread flour with your preferment")
    print(f"correct amount of oil is a WIP")
    print(f"Knead for 10 minutes")
    print(f"Let rise")
    if unit == "g":
        dough_ball_weight = round(dough_ball_weight / 28.3495, 1)
    print(f"Partition dough into {dough_balls} balls: {round(total_weight/dough_balls)} grams / {dough_ball_weight} oz each")
    print(f"Rest dough balls")
    print(f"Make some epic pizza!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Prints a pizza recipe based on parameters such as hydration and number of dough balls')
    parser.add_argument('--hydration', type=float, default=0.66, help='The hydration of the dough, or the ratio of water to flour, expressed as a decimal (default 0.66)')
    parser.add_argument('--salt', type=float, default=0.02, help='The salt percentage of the dough, or the ratio of salt to flour, expressed as a decimal (default 0.02)')
    parser.add_argument('--dough_balls', type=int, default=8, help='The number of dough balls to make (default 8)')
    parser.add_argument('--dough_ball_weight', type=int, default=6, help='The weight of each dough ball in specified units (default 6)')
    parser.add_argument('--unit', type=str, default="oz", help='The unit of measure for the dough ball weight - either "oz" or "g" (default "oz")')
    args = parser.parse_args()
    pizzaRecipe(args.hydration, args.salt, args.dough_balls, args.dough_ball_weight, args.unit)