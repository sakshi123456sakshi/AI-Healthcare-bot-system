<?php
$host="localhost";
$username="root";
$password="";
$database="chatbot";
$connection= new mysqli($host,$username,$password,$database);
if($connection->connect_error)
{
    die('Connection Failed:'.$connection->connect_error);
}
// if($_SERVER['REQUEST_METHOD']=="POST"){
    $fullName=$_POST["fullName"];
    $Username=$_POST["Username"];
    $Password=$_POST["Password"];
    $dob=$_POST["dob"];
    $age=$_POST["age"];
    $blood_group=$_POST["blood_group"];
    $gender=$_POST["gender"];
    $phone=$_POST["phone"];
    $address=$_POST["address"];


    $sql="INSERT INTO register(fullName,Username,Password,dob,age,blood_group,gender,phone,address) VALUES('$fullName','$Username','$Password','$dob','$age','$blood_group','$gender','$phone','$address')";
    $result=$connection->query($sql);

    if($result==TRUE)
    {
        echo "Register Successful!";

            header("Location:loginuser.html");
    }
    else{
        echo "Registred Failed";
    }
// }


mysqli_close($connection);

?>