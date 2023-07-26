SELECT min(week(test_end_date)) as mdat FROM viam.orders
where month(test_end_date)=$mn;