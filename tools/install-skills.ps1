param([string]$Destination = "$HOME\.codex\skills")
$Root = Split-Path -Parent $PSScriptRoot
$Source = Join-Path $Root '.codex\skills'
New-Item -ItemType Directory -Force -Path $Destination | Out-Null
Get-ChildItem -LiteralPath $Source -Directory | ForEach-Object {
  $target = Join-Path $Destination $_.Name
  New-Item -ItemType Directory -Force -Path $target | Out-Null
  Copy-Item -LiteralPath (Join-Path $_.FullName 'SKILL.md') -Destination $target -Force
  Write-Host "Installed $($_.Name)"
}
$team = Join-Path $PSScriptRoot "team-knowledge-base.SKILL.md"`nif (Test-Path $team) { $target = Join-Path $Destination "team-knowledge-base"; New-Item -ItemType Directory -Force -Path $target | Out-Null; Copy-Item $team (Join-Path $target "SKILL.md") -Force; Write-Host "Installed team-knowledge-base" }`nWrite-Host "Done. Restart Codex or start a new chat to discover the skills."

