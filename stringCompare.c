int comparestring(char *s1,char *s2)
{
  //check the string character by character
	while(*s1!='\0' && *s2!='\0')
	{
	if(*s1!=*s2)	
	return -1;
	s1++;
	s2++;
	}

return (*s1-*s2);

}
