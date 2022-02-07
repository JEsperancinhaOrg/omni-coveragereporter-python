<?php

$upload_dir = 'tmp/';
$upload_file = $upload_dir . basename($_FILES['user-file']['name']);

class Person 	{
	
	var $personId;
	var $firstname;
	var $lastname;
	
	function __construct($personID, $firstname, $lastname)
	{
		 $this->personId = $personID;
		 $this->firstname = $firstname;
		 $this->lastname = $lastname;
	}
	
	
}
echo "<p>";


function cmp($a, $b)
{
	return strcmp($a->firstname, $b->firstname);
}



if (move_uploaded_file($_FILES['user-file']['tmp_name'], $upload_file)) {
  echo "Thank you " . $_POST['email'] . ". The result of the sorting is:";
} else {
   echo "Upload failed!!";
}

$gestor = @fopen($upload_file, "r");
$arrayTest =array();
$buffer = fgets($gestor, 4096);
if ($gestor) {
	while (($buffer = fgets($gestor, 4096)) !== false) {
		list($id,$name,$surname) = explode(",", $buffer);
		$person = new Person($id, $name, $surname);
		$arrayTest[] = $person;
	}
	if (!feof($gestor)) {
		echo "Error: Unexpected failure!\n";
	}
	fclose($gestor);
}

usort($arrayTest, "cmp");

echo '</br>';

foreach ($arrayTest as &$value) {
	echo $value->personId;
	echo ',';
	echo $value->firstname;
	echo ',';
	echo $value->lastname;
	echo '</br>';
}

echo "</p>";

