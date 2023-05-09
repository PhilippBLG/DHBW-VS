def phone_words(string_of_nums):
    count = 0
    prev_num = ""
    count_list = []
    if string_of_nums == "":
        return ""
    number = [int(string_of_nums[0])]
    lst_2 = [[" "," "," "],[" "," "," "],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
    text = []
    for num in string_of_nums:
        if num != prev_num or count >= 3:
            if count != 0:
                count_list.append(count)
                number.append(int(num))
            count = 1
            prev_num = num
        else:
            count += 1
    count_list.append(count)
    for i in range(len(string_of_nums)):
        if i > len(string_of_nums) - 20:
            break
        text.append(lst_2[number[i]][count_list[i]-1])
    return "".join(text)

print(phone_words("443355555566604466690277733099966688"))