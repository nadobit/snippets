# Vorbereitungen

__SWRevealViewController.h__ und __SWRevealViewController.m__ über die GUI in ProjektStruktur kopieren und Bridge Header erstellen lassen.

```swift
#import "SWRevealViewController.h"
```

# Implementierung

1. Leere MenuControllerView erzeugen (Dienst nur als Bindeglied)
  __Klasse:__ SWRevealViewController

2. TableViewController Menü erzeugen
  - Evtl. Statisches Tabelle, oder whatever you wish
  - Segue zwischen MenuController und Menü erzeugen:
    __Name:__ sw_rear, __Klasse:__ SWRevealViewControllerSegueSetController, __Typ:__ custom

3. View (vorzugsweise Navigation Controller) erzeugen
  - Segue zum MenüController erzeugen
    __Name:__ sw_front, __Klasse:__ SWRevealViewControllerSegueSetController, __Typ:__ custom
  - Wahrscheinlich ist auch gewünscht, ein Segue vom Menü Eintrag zur View zu erstellen, hierbei handelt es sich dann allerdings um einen ganz herkömmlichen mit der Klasse SWRevealViewControllerSeguePushController


```swift
# Code zu aktivieren des berühmten Hamburger Menü in jeder abgezweigten View
@IBOutlet weak var navigationItemMenu: UIBarButtonItem!

override func viewDidLoad()
{
    super.viewDidLoad()

    if self.revealViewController() != nil {
        self.navigationItemMenu.target = self.revealViewController()
        self.navigationItemMenu.action = #selector(SWRevealViewController.revealToggle(_:))
        self.view.addGestureRecognizer(self.revealViewController().panGestureRecognizer())
    }
}
```

[SWRevealViewController]

[SWRevealViewController]:https://github.com/John-Lluch/SWRevealViewController