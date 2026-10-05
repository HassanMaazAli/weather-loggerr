def summarize(temps):
    """Returns a dictionary with minimum, maximum, and average temperatures."""
    if not temps:
        return {"minimum": None, "maximum": None, "average": None}
    
    return {
        "minimum": min(temps),
        "maximum": max(temps),
        "average": sum(temps) / len(temps)
    }

def main():
    temperatures = []
    
    while True:
        user_input = input("Enter temperature ('done' to stop): ").strip()
        
        if user_input.lower() == 'done':
            break
            
        try:
            temp = float(user_input)
            # Convert to int if there's no decimal part to match output format preference
            if temp.is_integer():
                temp = int(temp)
            temperatures.append(temp)
        except ValueError:
            print("Please enter a valid number or 'done'.")
            
    summary = summarize(temperatures)
    print(summary)

if __name__ == "__main__":
    main()