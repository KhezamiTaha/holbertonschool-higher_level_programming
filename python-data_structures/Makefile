
Function_file = 12-switch.py
Main_file =  12-main.py
NAME =  Python - Data Structures: Lists, Tuples
Function_name = binary_tree_t *binary_tree_node(binary_tree_t *parent, int value);


Header = binary_trees.h
Directory = singly_linked_lists






CC = gcc
Function_file_final =   '$(Function_file)' | tr -d '0123456789-'  
SRC =    $(Main_file) $(Function_file)  
OBJ = $(SRC:.c=.o)
RM = rm
git = git add * && git commit -m '$(NAME)' && git push
CFLAGS = -Wall -Werror -Wextra -pedantic -std=gnu89  
Final_header = \#include \"$(Header)\"
ReadMe = README.md


all: $(OBJ)
	$(CC)  $(CFLAGS)  $(OBJ) -o  $(NAME)
	betty  $(Header) $(Main_file)  $(Function_file)
	valgrind ./$(NAME) 
	$(RM) -rf $(OBJ) $(NAME)
	



.PHONY: clean oclean fclean re brk  echo valgrind folder

clean:
	$(RM) -rf *~  $(NAME)

oclean:
	$(RM) -rf $(OBJ) $(NAME)

fclean:
	$(RM) -rf *~  $(NAME)
	$(RM) -rf $(OBJ)
	rm $(SRC)
re: oclean  all

folder:
	mkdir $(Directory)
	cd $(Directory)
	touch $(ReadMe)

script:
	chmod u+x $(Function_file)
	pycodestyle $(Function_file)
	./$(Function_file)
main:
	chmod u+x $(Main_file)
	chmod u+x $(Function_file)
	black $(Function_file)
	pycodestyle $(Function_file)
	./$(Main_file)
file:
	chmod u+x $(Function_file)
	black $(Function_file)
	pycodestyle $(Function_file)
	./$(Function_file)

touch:
	touch $(Function_file)
	touch  $(Main_file)
git:
	rm -rf __pycache__
	$(git)

echo:
	
	echo  $(NAME)

valgrind:
	valgrind ./$(NAME)

brk:
	touch $(SRC) 
	grep -v '#endif' $(Header) > temp_file && mv temp_file $(Header)
	echo  "$(Function_name)"  >> "$(Header)"
	echo  "#endif"  >> "$(Header)"

	echo "$(Final_header)" >> "$(Function_file)"
	echo      ""            >> "$(Function_file)"
	echo  "/**"               >> "$(Function_file)"
	echo    " *"            >> "$(Function_file)"
	echo     $(Function_file_final)            >> "$(Function_file)"
	echo    " - Algorithms function"            >> "$(Function_file)"
	echo  " *@: pointer"              >> "$(Function_file)"
	echo  " *@: pointer"              >> "$(Function_file)"
	echo  " *"            >> "$(Function_file)"
	echo  " *Return: 1 or 0"             >> "$(Function_file)"
	echo  " */"            >> "$(Function_file)"
	echo      ""            >> "$(Function_file)"
	echo      ""            >> "$(Function_file)"
	echo      ""            >> "$(Function_file)"
	echo  "/**"   >> "$(Function_file)"
	echo  " * To-Do :  Variables Description"   >> "$(Function_file)"
	echo  " *          Formt document"   >> "$(Function_file)"
	echo  " */"   >> "$(Function_file)"
