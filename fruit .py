import turtle

def draw_speech_bubble(user_text):
    window = turtle.Screen()
    window.bgcolor("white")

    pen = turtle.Turtle()
    pen.color("black")
    pen.penup()
    pen.goto(-100, 0)  # Điều chỉnh vị trí bong bóng nói

    pen.write("Mèo nói: " + user_text, font=("Arial", 16, "normal"))  # Hiển thị văn bản trong bong bóng

    # Vẽ bong bóng nói
    width = pen.xcor()
    height = 50
    pen.goto(-100, height)
    pen.pendown()
    pen.forward(width)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(width)
    pen.left(90)
    pen.forward(50)
    pen.left(90)

    window.mainloop()

# Nhập văn bản từ người dùng
user_input = input("Nhập điều gì đó: ")

# Vẽ bong bóng nói với văn bản được cung cấp
draw_speech_bubble(user_input)
