--Убиваем все активные сеансы подключенные к базе NameDB
DECLARE @spid VARCHAR(200)
DECLARE @kill_spid VARCHAR(200)

DECLARE kill_session CURSOR FOR

SELECT spid FROM [master].dbo.sysprocesses
WHERE dbid=db_id('NameDB')
--spid идентификатор сеанса SQL Server.

 OPEN kill_session;

FETCH NEXT FROM kill_session INTO @spid
WHILE @@FETCH_STATUS = 0

BEGIN

   SET @kill_spid='KILL ' + @spid + char(10)
   --PRINT @kill_spid
   EXEC (@kill_spid)
   
 FETCH NEXT FROM kill_session
 INTO @spid;
END;
 DEALLOCATE kill_session;