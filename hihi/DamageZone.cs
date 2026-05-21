using UnityEngine;

public class DamageZone : MonoBehaviour
{
    [SerializeField] private float damage;

    [SerializeField] private bool playerInside = false;

    private float timeCoolDown = 2f, timer = 0f;

    private void Update()
    {
        if (!playerInside) return; 

        timer -= Time.deltaTime;
        if( timer <= 0f)
        {
            if (Player.instance != null)
            {
                Player.instance.TakeDamage(-damage);
                timer = timeCoolDown;
            }
        }
    }
    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.CompareTag("Player"))
        {
            playerInside = true;
            timer = 0f;
        }
}

    private void OnTriggerExit2D(Collider2D collision)
    {
        if (collision.CompareTag("Player"))
        {
            playerInside = false;
            timer = 0f;
        }
    }
}
