<?php
session_start();  // Start session

$host = "localhost";
$username = "root";
$password = "";
$database = "chatbot";

// Establish connection
$connection = new mysqli($host, $username, $password, $database);
if ($connection->connect_error) {
    die("Connection Failed: " . $connection->connect_error);
}

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] == "POST") {
    // Securely retrieve user inputs
    $Username = $connection->real_escape_string($_POST["Username"]);
    $Password = $connection->real_escape_string($_POST["Password"]);

    // Check if user exists in the users table
    $sql1 = "SELECT * FROM register WHERE Username=? AND Password=?";
    $stmt = $connection->prepare($sql1);
    $stmt->bind_param("ss", $Username, $Password);
    $stmt->execute();
    $result1 = $stmt->get_result();

    if ($result1->num_rows > 0) {
        $_SESSION["Username"] = $Username;  // Store username in session

        // Insert user details into login table
        $sql2 = "INSERT INTO login (Username, Password) VALUES (?, ?)";
        $stmt2 = $connection->prepare($sql2);
        $stmt2->bind_param("ss", $Username, $Password);
        if ($stmt2->execute()) {
            echo "Login recorded successfully...";
        } else {
            echo "Error recording login.";
        }
        $stmt2->close();

        // Redirect to Flask app
        header("Location: http://127.0.0.1:5000/");
        exit();
    } else {
        echo "Invalid username or password";
    }

    $stmt->close();
}

$connection->close();
?>


