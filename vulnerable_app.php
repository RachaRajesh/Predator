<?php
// Simulated vulnerable login script
$username = $_POST['username'];
$password = $_POST['password'];

// 🚨 Vulnerable SQL Query (No Input Sanitization)
$conn = new mysqli("localhost", "root", "", "test_db");
$sql = "SELECT * FROM users WHERE username='$username' AND password='$password'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "Login Successful!";
} else {
    echo "Invalid Credentials!";
}
?>
