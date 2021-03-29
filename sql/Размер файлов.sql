select  
	name,	
	physical_name,
	SUM(size * 8.0 / 1024) as [Size, Mb]
from sys.master_files
group by 
	name,
	physical_name,	
	Size