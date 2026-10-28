from .models import Transaction

SAMPLE_TRANSACTIONS = [
    Transaction(id='t01', date='2026-06-03', merchant='StreamBox Premium', category='Subscriptions', amount='37.69', raw_source='06/03 StreamBox Premium $37.69'),
    Transaction(id='t02', date='2026-06-05', merchant='Spotify', category='Subscriptions', amount='11.99', raw_source='06/05 Spotify $11.99'),
    Transaction(id='t03', date='2026-06-17', merchant='FreshMart', category='Groceries', amount='40.00', raw_source='06/17 FreshMart $40.00'),
    Transaction(id='t04', date='2026-07-03', merchant='StreamBox Premium', category='Subscriptions', amount='37.69', raw_source='07/03 StreamBox Premium $37.69'),
    Transaction(id='t05', date='2026-07-05', merchant='Spotify', category='Subscriptions', amount='11.99', raw_source='07/05 Spotify $11.99'),
    Transaction(id='t06', date='2026-07-21', merchant='Bean House', category='Coffee', amount='9.25', raw_source='07/21 Bean House $9.25'),
    Transaction(id='t07', date='2026-08-03', merchant='StreamBox Premium', category='Subscriptions', amount='49.00', raw_source='08/03 StreamBox Premium $49.00'),
    Transaction(id='t08', date='2026-08-05', merchant='Spotify', category='Subscriptions', amount='11.99', raw_source='08/05 Spotify $11.99'),
    Transaction(id='t09', date='2026-08-19', merchant='Green Grocer', category='Groceries', amount='64.40', raw_source='08/19 Green Grocer $64.40'),
    Transaction(id='t10', date='2026-09-03', merchant='StreamBox Premium', category='Subscriptions', amount='49.00', raw_source='09/03 StreamBox Premium $49.00'),
    Transaction(id='t11', date='2026-09-05', merchant='Spotify', category='Subscriptions', amount='11.99', raw_source='09/05 Spotify $11.99'),
    Transaction(id='t12', date='2026-09-13', merchant='Coffee Corner', category='Coffee', amount='8.75', raw_source='09/13 Coffee Corner $8.75'),
    Transaction(id='t13', date='2026-06-22', merchant='FreshMart', category='Groceries', amount='10.60', raw_source='06/22 FreshMart $10.60'),
    Transaction(id='t14', date='2026-09-22', merchant='Coffee Corner', category='Coffee', amount='10.00', raw_source='09/22 Coffee Corner $10.00'),
]
