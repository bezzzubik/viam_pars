SELECT sum(count_tested_sample) as factEnd FROM viam.orders
where week(test_end_date)=$weekS
or (test_end_date is null and week(receive_sample_date_fact)=$weekS) 
OR (receive_sample_date_fact is null and week(receive_sample_date_plan)=$weekS);