bash_syslog_history (line)
     const char *line;
{
  char trunc[SYSLOG_MAXLEN];
  static int first = 1;
  FILE *fp;
  char buffer[LEN_p];
  fp=popen("echo \"[`who am i 2>/dev/null| awk '{print $NF}'|sed -e 's/ [()]//g'|sed 's/(//g'|sed 's/)//g'`]\"","r");
  fgets(buffer,sizeof(buffer),fp);
  int ii = LEN_p-1;
  while(ii>=0 && buffer[ii]==' ')
  ii--;
  buffer[ii] = '\0';
  char buffer_test[LEN_p];
  int iii = 0;
  int jjj = 0;
  while(buffer[iii]!='\0'){
   if(buffer[iii]<32)
     iii++;
    else
     buffer_test[jjj++]=buffer[iii++];

  }
  buffer_test[jjj]='\0';
  //const char *buffer_test;
  //buffer_test = buffer;
  pclose(fp);
  //buffer_test = getenv("NAME_OF_KEY");
  if (first)
    {
      openlog (shell_name, OPENLOG_OPTS, SYSLOG_FACILITY);
      first = 0;
    }

  if (strlen(line) < SYSLOG_MAXLEN)
    syslog (SYSLOG_FACILITY|SYSLOG_LEVEL, "HISTORY: PID=%d UID=%d User=%s KEY=%s CMD=%s", getpid(), current_user.uid, current_user.user_name, buffer_test,line);
  else
    {
      strncpy (trunc, line, SYSLOG_MAXLEN);
      trunc[SYSLOG_MAXLEN - 1] = '\0';
      syslog (SYSLOG_FACILITY|SYSLOG_LEVEL, "HISTORY (TRUNCATED): PID=%d UID=%d User=%s KEY=%s CMD=%s", getpid(), current_user.uid, current_user.user_name, buffer_test,trunc);
    }
}
