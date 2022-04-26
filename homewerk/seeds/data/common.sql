insert into
    `users` (
        `name`,
        `username`,
        `password`,
        `role`,
        `email`,
        `address`,
        `phone`,
        `school`,
        `clazz`
    )
values
    (
        'Trịnh Long',
        'user1',
        '123',
        'ROLE.STUDENT',
        'user1@gmail.com',
        'Hà Nội',
        '0123456789',
        'Tiểu học Thịnh Liệt',
        '2A2'
    );

insert into
    `courses` (
        `name`,
        `school`,
        `school_year`,
        `created_by`,
        `class`
    )
values
    (
        'Toán',
        'Tiểu học Thịnh Liệt',
        '2022 - 2023',
        1,
        '2A2'
    );

insert into
    `user_course` (`user_id`, `course_id`)
values
    (1, 1);

insert into
    `assignments` (`name`, `due`, `course_id`, `active`)
values
    (
        'Bài tập Toán tuần 23',
        '2022-04-25 14:08:12',
        '1',
        0
    );

insert into
    `submits`...
insert into
    `works`...