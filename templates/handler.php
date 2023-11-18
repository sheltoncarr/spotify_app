<?php

    $errors = [];
    $errorMessage = '';
    echo "got here"

    if (isset($_POST["submit"])) {
            $fname = $_POST["firstname"];
            $lname = $_POST["lastname"];
            $country = $_POST["country"];
            $email = $_POST["email"];
            $submission = $_POST["message"];

        if (empty($fname)) {
            $errors[] = 'First name is empty';
        }

        if (empty($lname)) {
            $errors[] = 'Last name is empty';
        }

        if (empty($country)) {
            $errors[] = 'Country is empty';
        }

        if (empty($email)) {
            $errors[] = 'Email is empty';
        } else if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $errors[] = 'Email is invalid';
        }

        if (empty($submission)) {
            $errors[] = 'Message is empty';
        }

        if (empty($errors)) {
            $to = 'muuscodes@gmail.com';
            $subject = 'New email from your contact form';
            $additional_headers = ['Reply-To' => $email, 'Content-type' => 'text/html; charset=utf-8'];
            $bodyParagraphs = ["Name: {$fname} ${lname}", "Email: {$email}", "Country: {$country}", '<br/>', "Message:", $submission];
            $message = join(PHP_EOL, $bodyParagraphs);

            mail($to, $subject, $message, $additional_headers);

            echo "Fuck me";

        } else {

            $allErrors = join('<br/>', $errors);
            $errorMessage = "<p style='color: red;'>{$allErrors}</p>";
        }
        // header("Location: index.html")
    }

?>
