def count_buildings_with_sunset_view(building_heights):
    count = 0
    for i in range(len(building_heights)):
        curr_building = building_heights[i]
        if not any(building_heights[j] > curr_building for j in range(0, i-1)):
            count += 1
    return count


def count_buildings_with_sunset_view_optimal(building_heights):
    count = 1
    max_height_so_far = building_heights[0]
    for i in range(1, len(building_heights)):
        if building_heights[i] > max_height_so_far:
            count += 1
            max_height_so_far = building_heights[i]
    return count


print(count_buildings_with_sunset_view([2, 4, 6, 10, 5]))
