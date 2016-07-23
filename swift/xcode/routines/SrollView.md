# Vertikale Scrollview

## Vorbereitungen
Scrollview an alle vier Ecken der SuperView pinnen.
ContentView in Scrollview ohne Abstände pinnen und EqualWidth zur SuperView setzen.

Erste Demo könnte eine weitere SubView der Content View sein (Margin: 8, Height: 2000) 👏

## Tips
- Um AutoLayout effektiv zu benutzen ist es sinnvoll von der ersten View (dem ersten Element) anzufangen Abstände nach unten festzulegen und diese erst zu löschen, wenn untere Elemente hinzugefügt werden, die dann wieder einen Abstand nach unten bekommen. So vermeidet man Fehler und Warnungen des Auto Layouters
