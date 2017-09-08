#include <iostream>
#include <string.h>
using namespace std;

int modulo(int a,int b){
	int q = a/b;
	int r = a - (q*b);
	if(r < 0)
		r = r+b;
	return r;
}
int euclides(int a,int b){
	int r=modulo(a,b);
	while(r>0){
		a=b;
		b=r;
		r=modulo(a,b);
	}
	return b;
}
void m_m(void){
	cout<<"ingrese los numeros a multiplicar: "<<endl;
	int a, b, m;
	cin>>a; cin>>b;
	cout<<"ingrese el modulo: "<<endl;
	cin>>m;
	cout<<"("<<a<<"*"<<b<<") mod "<<m<<endl;
	int na=modulo(a,m);
	int nb=modulo(b,m);
	int resul=modulo(na*nb,m);
	cout<<"=>   [("<<a<<"mod "<<m<<")*("<<b<<"mod "<<m<<")] mod"<<m<<endl;
	cout<<"=>   [("<<na<<")*("<<nb<<")] mod "<<m<<endl;
	cout<<"=>   ["<<na * nb<<"] mod "<<m<<endl;
	cout<<"=>   "<<resul<<endl;
}
void inversa(void){
	cout<<"ingrese el numero: "<<endl;
	int a, m;
	cin>>a;
	cout<<"ingrese el modulo: "<<endl;
	cin>>m;
	for(int i=0;i<m;i++){
		int nn=modulo(a*i,m);
		cout<<a<<"*"<<i<<"="<<a*i<<" mod "<<m<<" -> "<<nn<<"mod "<<m<<endl;
		if(nn == 1){
			cout<<"^  ^  ^  ^  ^  ^  ^  ^  "<<i<<" es la inversa  <-----------------------"<<endl;
		}
	}
}
int power(int base,int exp){
	int r=1;
	if(exp==0)
		return 1;
	while(exp>0){
		r*=base;
		exp--;
	}
	return r;
}
void poten(void){
	cout<<"ingrese los numeros para potenciar, base y exponente: "<<endl;
	int b, e, m;
	cin>>b; cin>>e;
	cout<<"ingrese el modulo: "<<endl;
	cin>>m;
	cout<<endl;
	cout<<"("<<b<<"^"<<e<<") mod "<<m<<endl;
	int nb=modulo(b,m);
	cout<<"=>   [("<<b<<"mod "<<m<<")^"<<e<<")] mod"<<m<<endl;
	cout<<"=>   ("<<nb<<"^"<<e<<") mod "<<m<<endl;
	int resul=1;
	string binario="";
	int ee=e;
	while(ee>0){
		if(modulo(ee,2)==1)
			binario+="1";
		binario+="0";
		ee=ee/2;
	}
	cout<<endl;
	cout<<e<<"--binario-->  "+binario<<endl;
	cout<<endl;
	int cont=0,bb=b;
	while(e>0){
		if(modulo(e,2)==1){
			cout<<bb<<" ^ "<<power(2,cont)<<" mod "<<m;
			resul=modulo(b*resul,m);
			cout<<" => "<<resul<<" mod "<<m<<endl;
		}
		e=e/2;
		b=modulo(b*b,m);
		cont++;
	}
	cout<<endl;
	cout<<" --> resultado "<<resul<<endl;
}
int main(int argc, char *argv[]) {
	//m_m();
	//inversa();
	poten();
	return 0;
}

