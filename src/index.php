<form enctype="multipart/form-data" action="upload.php" method="POST">
	<input type="hidden" name="MAX_FILE_SIZE" value="512000" />
	<p>
		Send this file: <input name="user-file" type="file" /> <input
			type="submit" value="Send File" />
	</p>
	<p>
		Enter your email: <input name="email" type="text" />
	</p>
</form>
