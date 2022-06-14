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
    # insert into `user_course` (`user_id`, `course_id`, `active`) values
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
    #insert into `assignments` (`id`, `course_id`, `name`, `due`, `active`, `instruction`) values
    # Course 1
    for i in range(1, 10):
        print(f"({i}, 1, 'Bảng cộng {i}', '2022-0{random.randint(1, 9)}-{random.randint(10, 27)} 0{random.randint(1, 9)}:00:00', 1," + 
        f"'Làm bài {random.randint(1,5)} SGK trang {random.randint(1, 100)} theo {random.randint(1,3)} cách khác nhau'),")
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

def gen_notification():
    #create assignment
    # Course 1
    for i in range(1, 10):
        print(f"('assignment', '{{''course'': 1, ''assignment'': {i}}}', 51, 'Assignment created', 'Teacher 51 create assignment {i}', {i}, 'Assignment'),")
    # Course 2
    for i in range(1, 6):
        print(f"('assignment', '{{''course'': 2, ''assignment'': {i+9}}}', 51, 'Assignment created', 'Teacher 51 create assignment {i+9}', {i+9}, 'Assignment'),")
    # Course 3
    for i in range(1, 6):
        print(f"('assignment', '{{''course'': 3, ''assignment'': {i+14}}}', 51, 'Assignment created', 'Teacher 51 create assignment {i+14}', {i+14}, 'Assignment'),")
    # Course 4
    for i in range(1, 6):
        print(f"('assignment', '{{''course'': 4, ''assignment'': {i+19}}}', 51, 'Assignment created', 'Teacher 51 create assignment {i+19}', {i+19}, 'Assignment'),")
    # Course 5
    for i in range(1, 6):
        print(f"('assignment', '{{''course'': 5, ''assignment'': {i+24}}}', 51, 'Assignment created', 'Teacher 51 create assignment {i+24}', {i+24}, 'Assignment'),")

    # student join
    # Course 1
    for i in range(1, 51):
        print(f"('course', '{{''course'': 1}}', {i}, 'Student join course', 'Student {i} join course 1', 1, 'Course'),")
    # Course 2
    for i in range(1, 51):
        print(f"('course', '{{''course'': 2}}', {i}, 'Student join course', 'Student {i} join course 2', 2, 'Course'),")
    # Course 3
    for i in range(1, 41):
        print(f"('course', '{{''course'': 3}}', {i}, 'Student join course', 'Student {i} join course 3', 3, 'Course'),")
    # Course 4
    for i in range(1, 41):
        print(f"('course', '{{''course'': 4}}', {i}, 'Student join course', 'Student {i} join course 4', 4, 'Course'),")
    # Course 5
    for i in range(1, 41):
        print(f"('course', '{{''course'': 5}}', {i}, 'Student join course', 'Student {i} join course 5', 5, 'Course'),")
    pass

def gen_notification_subcriber():
    # Course
    # Course 1
    for i in range(1, 51):
        print(f"({i}, 'course', 1, 1),")
    # Course 2
    for i in range(1, 51):
        print(f"({i}, 'course', 2, 1),")
    # Course 3
    for i in range(1, 41):
        print(f"({i}, 'course', 3, 1),")
    # Course 4
    for i in range(1, 41):
        print(f"({i}, 'course', 4, 1),")
    # Course 5
    for i in range(1, 41):
        print(f"({i}, 'course', 5, 1),")

    #Assignment
    # Course 1
    for i in range(1, 10):
        print(f"(51, 'assignment', {i}, 1),")
    # Course 2
    for i in range(1, 6):
        print(f"(51, 'assignment', {i}, 1),")
    # Course 3
    for i in range(1, 6):
        print(f"(51, 'assignment', {i}, 1),")
    # Course 4
    for i in range(1, 6):
        print(f"(51, 'assignment', {i}, 1),")
    # Course 5
    for i in range(1, 6):
        print(f"(51, 'assignment', {i}, 1),")

def gen_submit():
    id = 0
    for i in range(1, 51):
        id = id + 1
        print(f"(1, {i}, 'graded', {random.randint(5, 9)}, {id}, 'Cần nhiều cố gắng hơn'),")

    for i in range(1, 51):
        id = id + 1
        print(f"(2, {i}, 'graded', {random.randint(5, 9)}, {id}, 'Cần nhiều cố gắng hơn'),")

    for i in range(1, 51):
        id = id + 1
        print(f"(10, {i}, 'graded', {random.randint(5, 9)}, {id}, 'Cần nhiều cố gắng hơn'),")

    for i in range(1, 51):
        id = id + 1
        print(f"(11, {i}, 'graded', {random.randint(5, 9)}, {id}, 'Cần nhiều cố gắng hơn'),")

def gen_work():
    id = 0
    for i in range(1, 51):
        id = id + 1
        print(f"({i}, 'https://storage.googleapis.com/hoemwerk-bucket/image/submit/89c61a72-68b1-4abb-82b1-616a399eaff1', 1, "
              f"'{{\"version\":\"5.2.1\",\"objects\":[]}}', {id}, 1,"
              f"'https://storage.googleapis.com/hoemwerk-bucket/image/submit/ab2ceaf2-86c5-4ca5-8304-b1e440fa9f59'),")
        id = id + 1
        print(f"({i}, 'https://storage.googleapis.com/hoemwerk-bucket/image/submit/b7d1539a-f996-4f91-b1e0-1afe11924ce1', 2, "
              f"'{{\"version\":\"5.2.1\",\"objects\":[]}}', {id}, 1,"
              f"'https://storage.googleapis.com/hoemwerk-bucket/image/submit/0c051e68-0f40-491d-bb52-538dc5c670fd'),")
        id = id + 1
        print(f"({i}, 'https://storage.googleapis.com/hoemwerk-bucket/image/submit/a22e6ac4-6747-49cb-86b4-63dbec9b8ef3', 3, "
              f"'{{\"version\":\"5.2.1\",\"objects\":[]}}', {id}, 1,"
              f"'https://storage.googleapis.com/hoemwerk-bucket/image/submit/9c1b68c5-dc98-469b-8195-0edad4324352'),")


    for i in range(51, 101):
        id = id + 1
        print(f"({i}, 'https://storage.googleapis.com/hoemwerk-bucket/image/submit/2c5f2d33-dbce-4560-90b1-8db5cfa72b75', 1, "
              f"'{{\"version\":\"5.2.1\",\"objects\":[]}}', {id}, 1,"
              f"'https://storage.googleapis.com/hoemwerk-bucket/image/submit/5b9b3e32-bf8d-4e33-af20-fdf8ff65919a'),")
        id = id + 1
        print(f"({i}, 'https://storage.googleapis.com/hoemwerk-bucket/image/submit/2cac118a-5090-4772-9a19-f0c4aa8d9a5c', 2, "
              f"'{{\"version\":\"5.2.1\",\"objects\":[]}}', {id}, 1,"
              f"'https://storage.googleapis.com/hoemwerk-bucket/image/submit/2cac118a-5090-4772-9a19-f0c4aa8d9a5c'),")
        id = id + 1
        print(f"({i}, 'https://storage.googleapis.com/hoemwerk-bucket/image/submit/2cac118a-5090-4772-9a19-f0c4aa8d9a5c', 3, "
              f"'{{\"version\":\"5.2.1\",\"objects\":[]}}', {id}, 1,"
              f"'https://storage.googleapis.com/hoemwerk-bucket/image/submit/2cac118a-5090-4772-9a19-f0c4aa8d9a5c'),")


    for i in range(101, 151):
        id = id + 1
        print(f"({i}, 'https://storage.googleapis.com/hoemwerk-bucket/image/submit/2c5f2d33-dbce-4560-90b1-8db5cfa72b75', 1, "
              f"'{{\"version\":\"5.2.1\",\"objects\":[]}}', {id}, 1,"
              f"'https://storage.googleapis.com/hoemwerk-bucket/image/submit/5b9b3e32-bf8d-4e33-af20-fdf8ff65919a'),")
        id = id + 1
        print(f"({i}, 'https://storage.googleapis.com/hoemwerk-bucket/image/submit/2cac118a-5090-4772-9a19-f0c4aa8d9a5c', 2, "
              f"'{{\"version\":\"5.2.1\",\"objects\":[]}}', {id}, 1,"
              f"'https://storage.googleapis.com/hoemwerk-bucket/image/submit/2cac118a-5090-4772-9a19-f0c4aa8d9a5c'),")


    for i in range(151, 201):
        id = id + 1
        print(f"({i}, 'https://storage.googleapis.com/hoemwerk-bucket/image/submit/2c5f2d33-dbce-4560-90b1-8db5cfa72b75', 1, "
              f"'{{\"version\":\"5.2.1\",\"objects\":[]}}', {id}, 1,"
              f"'https://storage.googleapis.com/hoemwerk-bucket/image/submit/5b9b3e32-bf8d-4e33-af20-fdf8ff65919a'),")
        id = id + 1
        print(f"({i}, 'https://storage.googleapis.com/hoemwerk-bucket/image/submit/2cac118a-5090-4772-9a19-f0c4aa8d9a5c', 2, "
              f"'{{\"version\":\"5.2.1\",\"objects\":[]}}', {id}, 1,"
              f"'https://storage.googleapis.com/hoemwerk-bucket/image/submit/2cac118a-5090-4772-9a19-f0c4aa8d9a5c'),")

gen_work()