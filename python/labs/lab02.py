# lab 02 Average Numbers

nums = []
nums_sum = float(0)
nums_avg = float(0)

while True:
    user_nums_input = input("Enter a number: ")
    try:
        num = float(user_nums_input)
        nums.append(num)
    except ValueError:
        if user_nums_input.lower() == "done":
            for num in nums:
                nums_sum += num
            nums_avg = nums_sum / len(nums)
            print(nums_avg)
            break
        else:
            print("you must enter a number")

