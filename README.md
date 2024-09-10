# online-shop

Projekt polega na przygotowaniu funkcjonalnego sklepu internetowego. Do zrobienia sklepu wykorzystujecie szablon strony przygotowany w poprzednim roku szkolnym. Oczywiście możecie go jeszcze modyfikować i rozbudowywać żeby sklep był jak najbardziej przejrzysty i funkcjonalny. 

W sklepie będzie można sprzedawać produkty zarówno fizyczne (wysyłane do klienta) lub elektroniczne (wysyłane do klienta na maila lub dostępne do pobrania w panelu klienta jeżeli zakupu dokonał klient zarejestrowany)

## Funkcje dla klienta

- Bezpieczny system rejestracji, logowania i przypominania hasła
- Panel klienta (dostępny po zalogowaniu), a w nim:
- możliwość edycji swoich danych osobowych i danych do wysyłki (adres wysyłki może być inny niż dane klienta)
- możliwość przeglądania historii swoich zamówień
- możliwość tworzenia listy produktów ulubionych
- Katalog produktów z możliwością wyszukiwania produktów po różnych parametrach. Z katalogu produktów można bezpośrednio dodać produkt do koszyka lub do listy ulubionych (tylko dla zalogowanych użytkowników)
- Karta produktu, na której są prezentowane szczegóły produktu wraz z galerią zdjęć produktów. Z poziomu karty produktu można dodawać produkty do koszyka lub do listy produktów ulubionych (tylko dla zalogowanych użytkowników)
- Koszyk na zakupy
- Proces zakupowy, w którym klient może wybrać rodzaj przesyłki, sposób płatności i podać niezbędne dane do zakupu.

Ważne: w sklepie mogą robić zakupy zarówno klienci zarejestrowani jak i klienci nie posiadający konta w klepie. 

## Funkcje panelu administracyjnego

- Bezpieczny system logowania i przypominania hasła (konta dla pracowników sklepu są zakładane przez administratora) 
- System zarządzania produktami, kategoriami i parametrami produktów. Każdy produkt można przypisać do jednej lub więcej kategorii w sklepie. W sklepie powinna być też możliwość tworzenia parametrów i przypisywania ich do produktów.
- System zarządzania klientami. Powinna być możliwość przeglądania listy kont klientów oraz edycji wybranych kont lub przypisywania do nich notatek.
- System zarządzania zamówieniami. Należy pamiętać, że w sklepie mogą składać zamówienia nie tylko klienci z zarejestrowanym w sklepie kontem ale też klienci bez konta. 
- System zarządzania sposobami o kosztami dostawy. 
- System zarządzania sposobami płatności. 
- Możliwość dodawania do sklepu z poziomu panelu administratora podstron informacyjnych takich jak regulamin, strona o nas, sposoby dostawy i inne dowolne podstrony, do których linki będą pojawiały się w menu sklepu i których treść będzie można edytować z poziomu panelu administratora. 
- Ocenie będą podlegały 3 etapy pracy
- System rejestracji i logowania do panelu klienta oraz panelu administratora
- Panel administracyjny
- Strona sklepu dostępna dla klienta

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```