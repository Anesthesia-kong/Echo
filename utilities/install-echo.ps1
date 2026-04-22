# install-echo.ps1 — install a distilled echo from examples/ into a Claude Code skills directory.
#
# Usage:
#   .\utilities\install-echo.ps1 <echo-name> [-Scope Project|Home]
#
#   -Scope Project   install into .\.claude\skills\<echo-name>\   (default; current project only)
#   -Scope Home      install into $HOME\.claude\skills\<echo-name>\   (every project on this machine)
#
# Examples:
#   .\utilities\install-echo.ps1 nietzsche-echo
#   .\utilities\install-echo.ps1 socrates-echo -Scope Home

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$EchoName,

    [Parameter(Position = 1)]
    [ValidateSet('Project', 'Home')]
    [string]$Scope = 'Project'
)

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$src = Join-Path $repoRoot "examples\$EchoName"

if (-not (Test-Path $src -PathType Container)) {
    Write-Error "$src not found"
    Write-Host "available echoes:"
    Get-ChildItem (Join-Path $repoRoot 'examples') -Directory | ForEach-Object { "  $($_.Name)" }
    exit 1
}

if ($Scope -eq 'Home') {
    $destRoot = Join-Path $HOME '.claude\skills'
} else {
    $destRoot = Join-Path $repoRoot '.claude\skills'
}

$dest = Join-Path $destRoot $EchoName

if (Test-Path $dest) {
    Write-Error "$dest already exists — remove it first if you want to reinstall"
    exit 1
}

New-Item -ItemType Directory -Path $destRoot -Force | Out-Null
Copy-Item -Path $src -Destination $dest -Recurse

$figure = $EchoName -replace '-echo$', ''
Write-Host "installed: $EchoName -> $dest"
Write-Host "activate by opening Claude Code and saying: from ${figure}'s perspective, ..."
