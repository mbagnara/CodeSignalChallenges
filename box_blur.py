'''
Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.

The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself. All the pixels on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down.

Example

For

image = [[1, 1, 1],
         [1, 7, 1],
         [1, 1, 1]]

the output should be boxBlur(image) = [[1]].

To get the value of the middle pixel in the input 3 × 3 square: (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1. The border pixels are cropped from the final result.

For

image = [[7, 4, 0, 1],
         [5, 6, 2, 2],
         [6, 10, 7, 8],
         [1, 4, 2, 0]]

the output should be

boxBlur(image) = [[5, 4],
                  [4, 4]]

There are four 3 × 3 squares in the input image, so there should be four integers in the blurred output. To get the first value: (7 + 4 + 0 + 5 + 6 + 2 + 6 + 10 + 7) = 47 / 9 = 5.2222 = 5. The other three integers are obtained the same way, then the surrounding integers are cropped from the final result.


Ref:
https://developer.apple.com/documentation/accelerate/blurring_an_image

'''


# def get_columns(image):

#     jumps = 1
#     new_position = 1

#     for k, v in enumerate(image[0]):

#         # If the Assignment fails it means iteration needs to be finish
#         try:
#             new_position = k + 3
#             _ = image[0][new_position]
#             jumps += 1
#         except IndexError:
#             break

#     return jumps


def get_sliced_matrix(image, row, col):
    new_matrix = []
    new_matrix.append(image[row + 0][col:col + 3])
    new_matrix.append(image[row + 1][col:col + 3])
    new_matrix.append(image[row + 2][col:col + 3])
    return new_matrix


def accumulate_all_matrix_elements(image):
    acc = 0
    for i in image:
        acc += i[0] + i[1] + i[2]
    return int(acc / 9)

def boxBlur(image):

    blurred_box = []
    row_number = 0

    for row in image:

        col_number = 0
        new_row = []
        is_valid_matrix = True

        # Checks every element of the row
        for i in row:

            # Fails if get_sliced_matrix() cant return a 3x3 matrix
            try:
                sliced_matrix = get_sliced_matrix(image, row_number, col_number)
            except IndexError:
                is_valid_matrix = False
                break

            # This matrix is not 3x3, so it will be ignored, and starts counting the next row
            if len(sliced_matrix[0]) < 3:
                break
            else:
                new_row.append(accumulate_all_matrix_elements(sliced_matrix))

            col_number += 1

        if is_valid_matrix:
            blurred_box.append(new_row)
        row_number += 1

    return blurred_box


image = [[36, 0, 18, 9, 9, 45, 27],
         [27, 0, 54, 9, 0, 63, 90],
         [81, 63, 72, 45, 18, 27, 0],
         [0, 0, 9, 81, 27, 18, 45],
         [45, 45, 27, 27, 90, 81, 72],
         [45, 18, 9, 0, 9, 18, 45],
         [27, 81, 36, 63, 63, 72, 81]]


print(boxBlur(image))
