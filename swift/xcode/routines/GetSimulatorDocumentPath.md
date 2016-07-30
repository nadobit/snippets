Simulator Verzeichnis ausgeben
Beispiel: /var/mobile/Containers/Data/Application/3CBD70C2-3A10-40F4-B054-FCB73770061A/Documents"
Dort wird auch die sqlite Datenbank abgelegt


```swift
let dirPaths = NSSearchPathForDirectoriesInDomains(.DocumentDirectory, .UserDomainMask, true)
debugPrint("App Path: \(dirPaths)")
```
