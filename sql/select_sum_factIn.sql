SELECT sum(fact_count_sample) as factIn FROM viam.orders 
where week(receive_sample_date_fact)=$weekS
OR (receive_sample_date_fact is null and week(receive_sample_date_plan)=$weekS);