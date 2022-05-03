import random

def gen_user():
    last_names = ['Trịnh', 'Nguyễn', 'Vũ', 'Trần', 'Lưu', 'Lê']
    middle_names = ['Thị', 'Hoàng', 'Đức', 'Đình', 'Đăng', 'Thanh', 'Thu']
    first_names = ['Long', 'Minh', 'Đức', 'Toàn', 'Thành', 'Tùng', 'Hiền', 'Diệp', 'Anh']
    for i in range(1, 51):
        l_name = random.choices(last_names)
        m_name = random.choices(middle_names)
        f_name = random.choices(first_names)
        name = ' '.join([l_name[0], m_name[0], f_name[0]])
        print(f"('{name}', {i}, 'student{i}', '123', 'ROLE.STUDENT', 'student{i}@gmail.com', 'Hà Nội', '0912345678', 'Tiểu học Thịnh Liệt', '2A2'),")
    
    for i in range(51, 55):
        l_name = random.choices(last_names)
        m_name = random.choices(middle_names)
        f_name = random.choices(first_names)
        name = ' '.join([l_name[0], m_name[0], f_name[0]])
        print(f"('{name}', {i}, 'teacher{i}', '123', 'ROLE.TEACHER', 'teacher{i}@gmail.com', 'Hà Nội', '0912345678', 'Tiểu học Thịnh Liệt', '2A{i-49}'),")
    
    for i in range(55, 58):
        l_name = random.choices(last_names)
        m_name = random.choices(middle_names)
        f_name = random.choices(first_names)
        name = ' '.join([l_name[0], m_name[0], f_name[0]])
        print(f"('{name}', {i}, 'student{i}', '123', 'ROLE.TEACHER', 'student{i}@gmail.com', 'Hà Nội', '0912345678', 'Tiểu học Thịnh Liệt', '2A1'),")
    
    for i in range(58, 61):
        l_name = random.choices(last_names)
        m_name = random.choices(middle_names)
        f_name = random.choices(first_names)
        name = ' '.join([l_name[0], m_name[0], f_name[0]])
        print(f"('{name}', {i}, 'student{i}', '123', 'ROLE.TEACHER', 'student{i}@gmail.com', 'Hà Nội', '0912345678', 'Tiểu học Thịnh Liệt', '2A1'),")


def gen_course():
    course_names = ['', 'Toán', 'Tiếng Việt', 'Tiếng Anh', 'Đạo đức', 'Tự nhiên Xã hội']
    for i in range(1, 6):
        print(f"({i}, '{course_names[i]} lớp 2', 'Tiểu học Thịnh Liệt', '2021', 51, '2A2', 1),")
    
    print(f"(6, '{course_names[1]} lớp 2', 'Tiểu học Thịnh Liệt', '2021', 52, '2A3', 1),")
    print(f"(7, '{course_names[3]} lớp 2', 'Tiểu học Thịnh Liệt', '2021', 52, '2A3', 1),")
    print(f"(8, '{course_names[2]} lớp 2', 'Tiểu học Thịnh Liệt', '2021', 53, '2A4', 1),")

def gen_course_user():
    # Course 1
    for i in range(1, 51):
        print(f"({i}, 1, 1),")
    # Course 2
    for i in range(1, 51):
        print(f"({i}, 2, 1),")
    # Course 3
    for i in range(1, 41):
        print(f"({i}, 3, 1),")
    # Course 4
    for i in range(1, 41):
        print(f"({i}, 4, 1),")
    # Course 5
    for i in range(1, 41):
        print(f"({i}, 5, 1),")
    # Course 6
    # Course 7
    # Course 8

def gen_assignment():
    # Course 1
    for i in range(1, 10):
        print(f"({i}, 1, 'Bảng cộng {i}', '2022-0{random.randint(1, 9)}-{random.randint(10, 27)} 0{random.randint(1, 9)}:00:00', 1," + 
        f"'Làm bài {random.randint(1,5)} SGK trang {random.randint(1, 100)}theo {random.randint(1,3)} cách khác nhau'),")
    # Course 2
    literature_asm_names = ['', 'Tôi là học sinh lớp 2', 'Ngày hôm qua đâu rồi?', 'Niềm vui của Bi và Bống', 'Làm việc thật là vui', 'Em có xinh không?']
    for i in range(1, 6):
        print(f"({i+9}, 2, '{literature_asm_names[i]}', '2022-0{random.randint(1, 9)}-{random.randint(10, 27)} 0{random.randint(1, 9)}:00:00', 1," + 
        f"'Trả lời câu {random.randint(1, 4)} trong SGK trang {random.randint(1, 100)}'),")
    # Course 3
    englist_asm_names = ['', 'At my birthday party', 'In the backyard', 'At the seaside', 'In the countryside', 'In the classroom']
    for i in range(1, 6):
        print(f"({i+14}, 3, '{englist_asm_names[i]}', '2022-0{random.randint(1, 9)}-{random.randint(10, 27)} 0{random.randint(1, 9)}:00:00', 1," + 
        f"'Trả lời câu {random.randint(1, 4)} trong SGK trang {random.randint(1, 100)}'),")
    # Course 4
    ethic_asm_names = ['', 'Vẻ đẹp quê hương em', 'Em yêu quê hương', 'Kính trọng thầy cô giáo', 'Yêu quý bạn bè', 'Quý trọng thời gian']
    for i in range(1, 6):
        print(f"({i+19}, 4, '{ethic_asm_names[i]}', '2022-0{random.randint(1, 9)}-{random.randint(10, 27)} 0{random.randint(1, 9)}:00:00', 1," + 
        f"'Trả lời câu {random.randint(1, 4)} trong SGK trang {random.randint(1, 100)}'),")
    # Course 5
    naturesocial_asm_names = ['', 'Các thế hệ trong gia đình', 'Nghề nghiệp của người lớn trong gia đình', 'Phòng tránh ngộ độc khi ở nhà', 'Giữ sạch nhà ở', 'Ôn tập chủ đề gia đình']
    for i in range(1, 6):
        print(f"({i+24}, 5, '{naturesocial_asm_names[i]}', '2022-0{random.randint(1, 9)}-{random.randint(10, 27)} 0{random.randint(1, 9)}:00:00', 1," + 
        f"'Trả lời câu {random.randint(1, 4)} trong SGK trang {random.randint(1, 100)}'),")
    pass

gen_assignment()