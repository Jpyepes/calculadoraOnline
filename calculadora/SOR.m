%SOR: Calcula la solución del sistema
%Ax=b con base en una condición inicial x0,mediante el método Gauss Seidel (relajado), depende del valor de w 
%entre (0,2)

function [E, s, T, respuesta, textoUsuario] = SOR(x0,A,b,Tol,niter,w)
    A = str2num(A);
    b = str2num(b);
    x0 = str2num(x0);
    c=0;
    error=Tol+1;
    D=diag(diag(A));
    L=-tril(A,-1);
    U=-triu(A,+1);
    while error>Tol && c<niter

        T=inv(D-w*L)*((1-w)*D+w*U);
        C=w*inv(D-w*L)*b;
        x1=T*x0+C;
        E(c+1)=norm(x1-x0,'inf');
        error=E(c+1);
        x0=x1;
        c=c+1;
    end
    radioEspectral = max(abs(eig(T)));
    if radioEspectral > 1
        respuesta = "El radio espectral de la matriz de transición es mayor a 1, verifique que este este ingresando correctamente la matriz o cambie de matriz.";
    else
        respuesta = "";
    end
    if error < Tol
        s=x0;
        n=c;
        s
        textoUsuario = 'Es una aproximación de la solución del sistmea con una tolerancia = ';
        s1 = num2str(Tol,'%0.2f');
        textoUsuario = strcat(textoUsuario,s1)
        fprintf('es una aproximación de la solución del sistmea con una tolerancia= %f',Tol)
    else 
        s=x0;
        n=c;
        textoUsuario = 'Fracasó en ';
        s1 = num2str(niter,'%0.9f');
        textoUsuario = strcat(textoUsuario,s1)
        s2 = ' iteraciones'
        textoUsuario = strcat(textoUsuario, s2)
        fprintf('Fracasó en %f iteraciones',niter) 
    end
end