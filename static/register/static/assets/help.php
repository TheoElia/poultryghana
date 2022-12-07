<?php

if(!$_POST) exit;

// Email verification, do not edit.
function isEmail($email_help ) {
	return(preg_match("/^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$/",$email_help ));
}

if (!defined("PHP_EOL")) define("PHP_EOL", "\r\n");

$fullname     	= $_POST['fullname'];
$email_help    	= $_POST['email_help'];
$message_help   = $_POST['message_help'];
$verify_help   	= $_POST['verify_help'];

if(trim($fullname) == '') {
	echo '<div class="error_message">Please enter your Fullname.</div>';
	exit();
} else if(trim($email_help) == '') {
	echo '<div class="error_message">Please enter a valid email address.</div>';
	exit();
} else if(!isEmail($email_help)) {
	echo '<div class="error_message">You have entered an invalid e-mail address.</div>';
	exit();
} else if(trim($message_help) == '') {
	echo '<div class="error_message">Please enter your message.</div>';
	exit();
} else if(!isset($verify_help) || trim($verify_help) == '') {
	echo '<div class="error_message">Please enter the verification number.</div>';
	exit();
} else if(trim($verify_help) != '4') {
	echo '<div class="error_message">The verification number you entered is incorrect.</div>';
	exit();
}

if(get_magic_quotes_gpc()) {
	$message_help = stripslashes($message_help);
}


//$address = "HERE your email address";
$address = "help@domain.com";


// Below the subject of the email
$e_subject = 'You\'ve been contacted by ' . $fullname . '.';

// You can change this if you feel that you need to.
$e_body = "You have been contacted by $fullname with additional message is as follows." . PHP_EOL . PHP_EOL;
$e_content = "\"$message_help\"" . PHP_EOL . PHP_EOL;
$e_reply = "You can contact $fullname via email, $email_help";

$msg = wordwrap( $e_body . $e_content . $e_reply, 70 );

$headers = "From: $email_help" . PHP_EOL;
$headers .= "Reply-To: $email_help" . PHP_EOL;
$headers .= "MIME-Version: 1.0" . PHP_EOL;
$headers .= "Content-type: text/plain; charset=utf-8" . PHP_EOL;
$headers .= "Content-Transfer-Encoding: quoted-printable" . PHP_EOL;

$user = "$email_help";
$usersubject = "Thank You";
$userheaders = "From: info@limmo.com\n";
$usermessage = "Thank you for contact LIMMO. We will reply shortly!";
mail($user,$usersubject,$usermessage,$userheaders);

if(mail($address, $e_subject, $msg, $headers)) {

	// Success message
	echo "<div id='success_page' style='padding:25px 0 0 0; text-align:center;'>";
	echo "<strong >Email Sent</strong><br>";
	echo "Thank you <strong>$fullname</strong>,<br> your message has been submitted.<br>We will contact you shortly.";
	echo "</div>";

} else {

	echo 'ERROR!';

}
