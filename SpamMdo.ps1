# Save current resolution
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Display {
    [DllImport("user32.dll")]
    public static extern int ChangeDisplaySettings(ref DEVMODE devMode, int flags);
    
    [StructLayout(LayoutKind.Sequential)]
    public struct DEVMODE {
        [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 32)]
        public string dmDeviceName;
        public short dmSpecVersion;
        public short dmDriverVersion;
        public short dmSize;
        public short dmDriverExtra;
        public int dmFields;
        public int dmPositionX;
        public int dmPositionY;
        public int dmDisplayOrientation;
        public int dmDisplayFixedOutput;
        public short dmColor;
        public short dmDuplex;
        public short dmYResolution;
        public short dmTTOption;
        public short dmCollate;
        [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 32)]
        public string dmFormName;
        public short dmLogPixels;
        public int dmBitsPerPel;
        public int dmPelsWidth;
        public int dmPelsHeight;
        public int dmDisplayFlags;
        public int dmDisplayFrequency;
        public int dmICMMethod;
        public int dmICMIntent;
        public int dmMediaType;
        public int dmDitherType;
        public int dmReserved1;
        public int dmReserved2;
        public int dmPanningWidth;
        public int dmPanningHeight;
    }
}
"@

# Change resolution to 1366x768
$devMode = New-Object Display+DEVMODE
$devMode.dmSize = [System.Runtime.InteropServices.Marshal]::SizeOf($devMode)
$devMode.dmPelsWidth = 1366
$devMode.dmPelsHeight = 768
$devMode.dmFields = 0x180000  # DM_PELSWIDTH | DM_PELSHEIGHT

Write-Host "Changing resolution to 1366x768..."
[Display]::ChangeDisplaySettings([ref]$devMode, 0)

Start-Sleep -Seconds 2

# Launch Clash of Clans via Google Play Games
Write-Host "Launching Clash of Clans..."
Start-Process "shell:AppsFolder\$(Get-StartApps | Where-Object { $_.Name -like '*Clash of Clans*' } | Select-Object -First 1 -ExpandProperty AppID)"

# Wait a moment for the window to open
Start-Sleep -Seconds 3

# Bring window to foreground
Add-Type @"
    using System;
    using System.Runtime.InteropServices;
    public class WinAPI {
        [DllImport("user32.dll")]
        [return: MarshalAs(UnmanagedType.Bool)]
        public static extern bool SetForegroundWindow(IntPtr hWnd);
        
        [DllImport("user32.dll")]
        [return: MarshalAs(UnmanagedType.Bool)]
        public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
        
        [DllImport("user32.dll")]
        public static extern IntPtr GetForegroundWindow();
    }
"@

# Try multiple times to find and focus the window
$attempts = 0
$maxAttempts = 10
$windowFound = $false

while (-not $windowFound -and $attempts -lt $maxAttempts) {
    $attempts++
    
    # Search for windows with "Clash" or "Google Play Games" in title
    $windows = Get-Process | Where-Object { 
        $_.MainWindowTitle -ne "" -and 
        ($_.MainWindowTitle -like '*Clash*' -or 
         $_.MainWindowTitle -like '*Google Play*' -or
         $_.ProcessName -like '*Google*')
    }
    
    foreach ($window in $windows) {
        Write-Host "Found window: $($window.MainWindowTitle) (Process: $($window.ProcessName))"
        [WinAPI]::ShowWindow($window.MainWindowHandle, 3)  # SW_MAXIMIZE
        [WinAPI]::SetForegroundWindow($window.MainWindowHandle)
        $windowFound = $true
        Write-Host "Window focused."
        break
    }
    
    if (-not $windowFound) {
        Start-Sleep -Milliseconds 500
    }
}

# Wait 12 more seconds (total 15 seconds)
Write-Host "Waiting..."
Start-Sleep -Seconds 60

# Launch UpgradeRempart.py script
Write-Host "Starting UpgradeRempart.py..."
Set-Location "$PSScriptRoot\cocfarmer_gpj"
python SpamMdo.py

# Restore original resolution
Write-Host "Restoring original resolution..."
[Display]::ChangeDisplaySettings([ref]$devMode, 0)
