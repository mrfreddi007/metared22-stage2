$timestamp = ([DateTimeOffset](Get-Date "Wed May 06 2020 05:01:20")).ToUnixTimeSeconds()
Write-Output $timestamp
$key = New-Object Byte[] 32
Get-Random -Max 256 -SetSeed $timestamp >$null
for ($index = 0; $index -lt 32; $index++) {$key[$index] = [byte](Get-Random -Max 256)}
$AES = New-Object System.Security.Cryptography.AesManaged
$AES.Key = $key
$AES.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7
$scriptPath = split-path -parent $MyInvocation.MyCommand.Definition
Write-Output $key
Get-ChildItem "$scriptPath" -Filter *_* | ForEach-Object {
    $file = "$_"
    $bytes = [System.IO.File]::ReadAllBytes("$file")
    $iv = $bytes[0..15]
    $AES.iv = $iv
    $decryptor = $AES.CreateDecryptor()
    $unencryptedData = $decryptor.TransformFinalBlock($bytes, 16, $bytes.Length - 16)
    Set-Content -Value $unencryptedData -AsByteStream $file.Substring(0,$file.IndexOf("_"))
}
# 53514c69746520666f726d6174203300
# e34d199cedf467fd2da2591b29e3515a