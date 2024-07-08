def is_palindrome(s):
  """
  Kiểm tra xem chuỗi s có phải là chuỗi hồi văn hay không.

  Args:
    s: Chuỗi cần kiểm tra.

  Returns:
    True nếu chuỗi s là chuỗi hồi văn, False nếu không.
  """

  # Đọc chuỗi vào từ bàn phím.
  s = input("Nhập chuỗi: ")

  # Chuyển đổi chuỗi thành hai chuỗi con: một chuỗi con chứa các ký tự từ trái sang phải và một chuỗi con chứa các ký tự từ phải sang trái.
  reversed_s = s[::-1]

  # So sánh hai chuỗi con.
  if s == reversed_s:
    return True
  else:
    return False

# Gọi hàm is_palindrome để kiểm tra chuỗi nhập vào.
if is_palindrome(s):
  print("Chuỗi", s, "là chuỗi hồi văn.")
else:
  print("Chuỗi", s, "không phải là chuỗi hồi văn.")
