# Mocking

Enhetstestning handlar om att testa varje *enhet* för sig: funktion, klass, modul osv.

Men vad gör vi om en funktion/klass är *beroende* (dependency) av en annan? Det räcker med att testa varje sak en gång.

Funktionen calculate_interest i account_manager.py är beroende av klassen BankAccount i bank_account.py. För att kunna testa calculate_interest utan att testa BankAccount igen, skapar vi en "fake class" i filen test_account_manager.py.
