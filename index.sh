ESCOLHA=$(dialog --stdout --menu 'Escolha Sua Opcao' 0 0 0 \
             1 'Listar' \
             2 'Listar com filtro' \
             3 'Enviar sinal' \
             4 'Mudar prioridade' \
             5 'Mudar CPU')

if [[ "$ESCOLHA" == "1" ]];then
	dialog --msgbox "`ps -auf`" 30 180
fi


if [[ "$ESCOLHA" == "2" ]];then
	dialog --msgbox "`ps -auf | grep ps`" 30 180
fi
