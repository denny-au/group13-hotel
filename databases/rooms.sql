CREATE TABLE rooms (
    id INT PRIMARY KEY AUTO_INCREMENT,
    number_of_beds INT,
    amenities TEXT,
    price_per_night DECIMAL (10, 2),
    image VARCHAR(255)
);