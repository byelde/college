package br.ufal.carro;

public interface Motor {

	// public boolean ligado;
	// public int aceleracao;

	// public Motor() {
	// 	this.ligado = false;
	// 	this.aceleracao = 0;
	// }

	public void ligar();
		// this.ligado = true;
	

	public void desligar();
		// this.ligado = false;


	public boolean isLigado();
		// return this.ligado;

	
	public void setAceleracao(int aceleracao);
		// this.aceleracao = aceleracao;
	

	public int getAceleracao();
		// return this.aceleracao;

	public abstract void acelerar(Carro c, int quantCombustivel);

}
