#include <iostream>
#include <vector>

using namespace std;
int modulo(int a,int b){
	int q,r;
	q=a/b;
	r=a-(q*b);
	if(r<0){
		q--;
		r+=b;
	}
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
vector<int> inversoMult(int a,int b){
	int u0=1, v0=0, u1=0, v1=1,q ,r ,u ,v;
	while(b>0){
		q=a/b;
		r=modulo(a,b);
		a=b;
		b=r;
		u=u0-q*u1;
		v=v0-q*v1;
		u0=u1;
		u1=u;
		v0=v1;
		v1=v;
	}
	vector<int> inv;
	inv.push_back(u0);
	inv.push_back(v0);
	return inv;
}
void diafanticas(void){
	cout<<"Ax + Bx = C"<<endl;
	int a,b,c;
	cout<<"ingrese valores para a    b    c"<<endl;
	cin>>a;
	cin>>b;
	cin>>c;
	cout<<a<<"x +"<<b<<"y ="<<c<<endl;
	int mcd= euclides(a,b);
	if(modulo(c,mcd)!=0){
		cout<<"No tiene solucion"<<endl;
	}
	else{
		int e=c/mcd;
		int x0,y0;
		vector<int> subzero;
		subzero=inversoMult(a,b);
		x0 = subzero[0];
		y0 = subzero[1];
		cout<<"mcd ="<<mcd<<endl;
		cout<<"e ="<<e<<endl;
		cout<<"Xo ="<<x0<<" y Yo ="<<y0<<endl;
		cout<<"Respuesta :"<<endl;
		cout<<"X = "<<x0 * e<<"   Y = "<<y0 * e<<endl;
	}
}
int main(int argc, char *argv[]) {
	diafanticas();
	return 0;
}

