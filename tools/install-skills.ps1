param([string]$Destination = "$HOME\.codex\skills")
$Root = Split-Path -Parent $PSScriptRoot
$Source = Join-Path $Root 'skills'
if (-not (Test-Path $Source)) { throw "skills folder not found: $Source" }
New-Item -ItemType Directory -Force -Path $Destination | Out-Null
Get-ChildItem -LiteralPath $Source -Directory | ForEach-Object {
  $skillFile = Join-Path $_.FullName 'SKILL.md'
  if (Test-Path $skillFile) {
    $target = Join-Path $Destination $_.Name
    New-Item -ItemType Directory -Force -Path $target | Out-Null
    Copy-Item -LiteralPath $skillFile -Destination (Join-Path $target 'SKILL.md') -Force
    Write-Host "Installed $($_.Name)"
  }
}
Write-Host "Done. Restart Codex or start a new chat to discover the skills."

